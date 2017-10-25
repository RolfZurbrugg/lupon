from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField
from wtforms.validators import DataRequired, Email, Length

from .models import Customer, User, Location
from lupon import db

class UserCreateForm(FlaskForm):
    email = TextField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ]
    )
    password = PasswordField(validators=[DataRequired(), Length(max=255)])
        
class LocationForm(FlaskForm):
    pass

class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
