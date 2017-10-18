from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask import g
from flask.ext import restful
# from flask_babel import gettext
from .extensions import babel


from config import LANGUAGES
from lupon import app, db
from .models import User
from .forms import EmailPasswordForm, CreateForm
import json

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
  form = CreateForm()
  # schema = UserSerializer()
  user = User.query.all()
  # json_string = schema.dump(user).data
  if form.validate_on_submit():
    user = User(
                form.email.data, 
                form.password.data
              )
    db.session.add(user)
    db.session.commit()
    flash("User successflly created!")
    return redirect(url_for('register'))
  return render_template('register.html', form=form, json=user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = CreateForm()
    if form.validate_on_submit():
        flash("SUCCESS")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/', methods=['GET','POST'])
def index():
  app.config['BABEL_DEFAULT_LOCALE'] = get_locale()
  return render_template("index.html")
'''
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
'''

'''
@SOURCE http://zqsmm.qiniucdn.com/data/20140904220136/index.html
'''

 
from lupon import api, db, flask_bcrypt, auth
from lupon.models import User, Post
from lupon.forms import UserCreateForm, SessionCreateForm, PostCreateForm
from lupon.serializers import UserSerializer, PostSerializer
 
@auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.user = user
    return flask_bcrypt.check_password_hash(user.password, password)
 
class UserView(restful.Resource):
    def post(self):
        form = UserCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
 
        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return UserSerializer(user).data
 
class SessionView(restful.Resource):
    def post(self):
        form = SessionCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
 
        user = User.query.filter_by(email=form.email.data).first()
        if user and flask_bcrypt.check_password_hash(user.password, form.password.data):
            return UserSerializer(user).data, 201
        return '', 401
 
class PostListView(restful.Resource):
    def get(self):
        posts = Post.query.all()
        return PostSerializer(posts, many=True).data
 
    @auth.login_required
    def post(self):
        form = PostCreateForm()
        if not form.validate_on_submit():
            return form.errors, 422
        post = Post(form.title.data, form.body.data)
        db.session.add(post)
        db.session.commit()
        return PostSerializer(post).data, 201
 
class PostView(restful.Resource):
    def get(self, id):
        posts = Post.query.filter_by(id=id).first()
        return PostSerializer(posts).data
 
api.add_resource(UserView, '/api/v1/users')
api.add_resource(SessionView, '/api/v1/sessions')
api.add_resource(PostListView, '/api/v1/posts')
api.add_resource(PostView, '/api/v1/posts/<int:id>')