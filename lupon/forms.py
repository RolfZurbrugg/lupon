from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from .models import Customer, User, Location
from lupon import db

from flask_login import current_user

class LoginForm(FlaskForm):
    email = TextField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ]
    )
    password = PasswordField(validators=[DataRequired(), Length(max=255)])

class UserForm(FlaskForm):
    email = TextField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ],
        render_kw={"placeholder": "e@ma.il", "type": "email"}
    )
    password = PasswordField('Password', validators=[DataRequired(), Length(max=255)])
    password_repeat = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=255), EqualTo('password_repeat', message='Passwords must match')])
    username = TextField('Username',validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Username"})
    firstname = TextField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= TextField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = TextField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = TextField('City',validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = TextField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = TextField('Street No.',validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = TextField('Zip',validators=[Length(max=255)], render_kw={"placeholder": "Zip", "class": "form-control is-valid"})

    def validate_username(self, parameter_list):
        pass
    
    def validate_email(self, parameter_list):
        pass
    
 
class LocationForm(FlaskForm):
    pass

class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
