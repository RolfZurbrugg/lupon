from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
# from flask_babel import gettext
from .extensions import babel


from config import LANGUAGES
from lupon import app, db
from .forms import EmailPasswordForm, RegistrationForm
from .models import Contact

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

@app.route('/login', methods=["GET", "POST"])
def login():
    flash("TEST")
    form = EmailPasswordForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/', methods=['GET','POST'])
def index():
  app.config['BABEL_DEFAULT_LOCALE'] = get_locale()
  return render_template("index.html")

'''
TEST FORM 1
'''

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        # db_session.add(user)
        flash('Thanks for registering: ')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact(id):
  obj = Contact.query.get(id)
  form = RegistrationForm(obj=obj)
  if form.validate_on_submit():

    if obj != None:
      form.populate_obj(obj)
    
    else:
      obj = Contact(form.username.data, 
                  form.email.data,
                  form.password.data,
                  phone = "1234" )

    db.session.add(obj)
    db.session.commit()
    return redirect(url_for('/contact'))
  return render_template("contact.html", form=form)


'''
@app.route('/dashboard')
@login_required
def account():
  return render_template("account.html")
'''