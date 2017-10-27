from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, ValidationError, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from .models import Contact, User, Location
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
    zip_code = TextField('Zip',validators=[Length(max=255)], render_kw={"placeholder": "Zip"})

    eula = BooleanField('Accept License Agreement')
    submit = SubmitField('Signup!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError(u'This username is taken')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is not None:
            raise ValidationError(u'This email is taken')
    
 
class UserProfileForm(FlaskForm):
    firstname = TextField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= TextField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = TextField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = TextField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = TextField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = TextField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = TextField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})
    submit = SubmitField('Update Profile')

class LocationForm(FlaskForm):
    pass

class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class ContactForm(FlaskForm):
    firstname = TextField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= TextField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = TextField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = TextField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = TextField('State', validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = TextField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = TextField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})
