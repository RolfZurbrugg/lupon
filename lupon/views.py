from flask import g
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, current_user, logout_user
from flask_babel import gettext
from .extensions import babel
import logging
from config import LANGUAGES
from lupon import app, db, flask_bcrypt
from lupon.models import User, Contact, Task, Location
from .forms import EmailPasswordForm, UserForm, LoginForm, UserProfileForm, TaskForm, ContactForm, LocationForm

@babel.localeselector
def get_locale():
  if request.args.get('lang'):
    lang = request.args['lang']
    if lang in LANGUAGES:
      return lang
    else:
      return 'en'
  
@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

@app.route('/', methods=['GET','POST'])
def index():
  app.config['BABEL_DEFAULT_LOCALE'] = get_locale()
  return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  
  form = UserForm()
  
  if form.validate_on_submit():

    try: 
        user = User()
        form.populate_obj(user)

        db.session.add(user)
        db.session.commit()
        flash("User successflly created!", 'success')
    
    except Exception as e:
        return e

    
    return redirect(url_for('index'))
  return render_template('register.html', form=form)

@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
  form = UserProfileForm(obj=current_user)

  if form.validate_on_submit():
    form.populate_obj(current_user)
    db.session.commit()
    flash('Profile updated.', 'success')

  return render_template('profile.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    flash('not authenticated', 'danger')

    if form.validate_on_submit():
        flash('form is valide', 'info')
        user, authenticated = User.authenticate(form.email.data,
                                    form.password.data)

        if user and authenticated:
            remember = request.form.get('remember') == 'y'
            if login_user(user, remember=remember):
                flash("Logged in", 'success')
            return redirect(url_for('index'))
        else:
            flash('Sorry, invalid login', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/task', methods=['GET','POST'])
@login_required
def task():

    # Prepoulate Form if task id is present in URL
    if request.args.get('task_id'):
        obj = Task.query.get(int(request.args['task_id']))
        taskform = TaskForm(obj=obj)

    else:
        taskform = TaskForm()

    # ToDo: only display where user_id = current_user
    tasks = Task.get_all(current_user.get_id())
    
    if taskform.validate_on_submit():
        logging.info('task from validated')
        task = Task()
        taskform.populate_obj(task)

        if task.update_task is True:
            tmp_task = Task.query.filter_by(id=task.id).first()
            taskform.populate_obj(tmp_task)
            tmp_task.modify_by = current_user.get_id()
            db.session.commit()
            flash("Task Updated! "+ str(task.update_task) , 'success')
            
        elif task.add_task is True:
            task.user_id = current_user.get_id()
            task.create_by = current_user.get_name()
            task.id = None
            db.session.add(task)
            db.session.commit()
            flash("Task created! "+ str(task.add_task), 'success')

        elif task.del_task is True:
            tmp_task = Task.query.filter_by(id=task.id).first()
            tmp_task.delete()
            flash("Task deleted "+ str(task.del_task), 'warning')
        
        return redirect(url_for('task'))
    return render_template("task.html", taskform=taskform, tasks=tasks)


@app.route('/admin', methods=["GET", "POST"])
@login_required
def admin():
    users = User.query.all()
    return render_template('admin.html', users=users)



@app.route('/contact', methods=['GET','POST'])
@login_required
def contact():

    if request.args.get('contact_id'):
        obj = Contact.query.get(int(request.args['contact_id']))
        contactform = ContactForm(obj=obj)
        loc_obj = Location.query.filter_by(contact_id=obj.get_id()).first()
        locationform = LocationForm(loc_obj)
    
    else:
        contactform = ContactForm()
        locationform = LocationForm()

    contacts = Contact.get_all(current_user.get_id())

    if contactform.validate_on_submit():
        logging.info('contact from validated')
        
        if obj is None:
            contact = Contact()
            location = Location(contact_id=contact.get_id())
            logging.info('creating new contact and location')
        
        else:
            contact = obj
            location = Location.query.filter_by(contact_id=contact.id).first()
            logging.info('query contact')
        
        contactform.populate_obj(contact)
        locationform.populate_obj(location)

        if contact.update_contact is True:
            tmp_contact = Contact.query.filter_by(id=contact.id).first()
            if Location.query.filter_by(contact_id=contact.id).first() is not None:
                locationform.populate_obj(Location.query.filter_by(contact_id=contact.id).first())
            contactform.populate_obj(tmp_contact)
            tmp_contact.modify_by = current_user.get_id()
            db.session.commit()
            flash("contact Updated! "+ str(contact.update_contact) , 'success')
            
        elif contact.add_contact is True:
            contact.user_id = current_user.get_id()
            contact.create_by = current_user.get_name()
            contact.id = None
            db.session.add(contact)

            db.session.commit()
            flash("contact created! "+ str(contact.add_contact), 'success')

        elif contact.del_contact is True:
            tmp_contact = Contact.query.filter_by(id=contact.id).first()
            if Location.query.filter_by(contact_id=contact.id).first() is not None:
                db.session.delete(Location.query.filter_by(contact_id=contact.id).first())
            db.session.delete(tmp_contact)
            db.session.commit()
            flash("contact deleted "+ str(contact.del_contact), 'warning')
        
        return redirect(url_for('contact'))

    return render_template('contact.html', contactform=contactform, contacts=contacts, locationform=locationform)