from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
# from flask_babel import gettext
from .extensions import babel


from config import LANGUAGES
from lupon import app
from .forms import EmailPasswordForm

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
@app.route('/dashboard')
@login_required
def account():
  return render_template("account.html")
'''