from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, StringField, ValidationError, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

from .models import Contact, User, Location
from lupon import db

from flask_login import current_user


class LoginForm(FlaskForm):
    email = StringField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ]
    )
    password = PasswordField(validators=[DataRequired(), Length(max=255)])


class UserForm(FlaskForm):
    email = StringField(
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ],
        render_kw={"placeholder": "e@ma.il", "type": "email"}
    )
    password = PasswordField('Password', validators=[DataRequired(), Length(max=255)])
    password_repeat = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=255), EqualTo('password', message='Passwords must match')])
    username = StringField('Username',validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Username"})
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City',validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.',validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip',validators=[Length(max=255)], render_kw={"placeholder": "Zip"})

    eula = BooleanField('Accept License Agreement')
    submit = SubmitField('Signup!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError(u'This username is taken')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is not None:
            raise ValidationError(u'This email is taken')
    
 
class UserProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})
    submit = SubmitField('Update Profile')


class LocationForm(FlaskForm):
    pass


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class ContactForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State', validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})


class TaskForm(FlaskForm):
    name = StringField('Name', validators=[Length(min=3, max=255)], render_kw={"placeholder": "Name"})
    amount = StringField('Amount', validators=[Length(min=1)], render_kw={"placeholder": "Amount"})
    # unit = StringField('Unit', validators=[Length(min=3, max=255)], render_kw={"placeholder": "Unit"})
    # description = StringField('Description', validators=[Length(min=3, max=255)], render_kw={"placeholder": "Description"})
    # value = StringField('Value', validators=[Length(min=0)], render_kw={"placeholder": "Value"})
    add_task = SubmitField('Add Task')
    # del_task = SubmitField('Delete Task')

    # __tablename__ = 'task'
    # name = Column(String(256)) #Name of the shit
    # amount = Column(Float)  #How much shit
    # unit = Column(String(256))  #Unit of shit
    # description = Column(Text) # Shiti descripion
    # value = Column(Float) #Cost of shit
    # user_id = Column(Integer, ForeignKey('user.id'), nullable=False)