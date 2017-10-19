from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
# from flask_babel import gettext
from .extensions import babel


from config import LANGUAGES
from lupon import app, db
from .models import User
from .forms import EmailPasswordForm, UserCreateForm

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

@app.route('/register', methods=["GET", "POST"])
def register():
  form = UserCreateForm()
  users = User.query.all()
  if form.validate_on_submit():
    user = User(
                form.email.data, 
                form.password.data
              )
    db.session.add(user)
    db.session.commit()
    flash("User successflly created!")
    return redirect(url_for('register'))
  return render_template('register.html', form=form, users=users)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = UserCreateForm()
    if form.validate_on_submit():
        flash("SUCCESS")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/', methods=['GET','POST'])
def index():
  app.config['BABEL_DEFAULT_LOCALE'] = get_locale()
  return render_template("index.html")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
