from flask_wtf import Form
from wtforms_alchemy import model_form_factory
from wtforms import StringField, PasswordField, TextField
from wtforms.validators import DataRequired, Email, Length

from .models import Customer, User, Location
from lupon import db

BaseModelForm = model_form_factory(Form)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class CreateForm(ModelForm):
    class Meta:
        model = User
        email = TextField(
            validators=[
                Email(),
                DataRequired(),
                Length(max=255)
            ]
        )
        name = TextField(
            validators=[
                DataRequired(),
                Length(max=255, min=6)
            ]
        ),

class LocationForm(ModelForm):
    class Meta:
        model = Location

''' DEPRECATED '''
class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


'''
@SOURCE https://gist.githubusercontent.com/basco-johnkevin/90773609d82f6d4894e5/raw/forms.py
'''
from flask.ext.wtf import Form
 
from wtforms_alchemy import model_form_factory
from wtforms import StringField
from wtforms.validators import DataRequired
 
from lupon import db
from lupon.models import User, Post
 
BaseModelForm = model_form_factory(Form)
 
class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session
 
class UserCreateForm(ModelForm):
    class Meta:
        model = User
 
class SessionCreateForm(Form):
    email = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
 
class PostCreateForm(ModelForm):
    class Meta:
        model = Post
