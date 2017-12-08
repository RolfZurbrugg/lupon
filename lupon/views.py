from flask import g
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, current_user, logout_user
from flask_babel import gettext
from .extensions import babel
import logging
from config import LANGUAGES
from lupon import app, db, flask_bcrypt
from lupon.models import User, Contact, Task
from .forms import EmailPasswordForm, UserForm, LoginForm, UserProfileForm, TaskForm

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


@app.route('/tasklist', methods=['GET','POST'])
def task():
    form = UserForm()
    taskform = TaskForm()

    # tasks = Task.query()

    if taskform.validate_on_submit():
        flash('valid')
        try:
            task2 = Task()
            # taskform.populate_obj(task2)

            db.session.add(task2)
            db.session.commit()
            flash("Task created!", 'success')

        except Exception as e:
            return e

        return redirect(url_for('index'))
    flash('nope')
    return render_template("tasklist.html", taskform=taskform)
