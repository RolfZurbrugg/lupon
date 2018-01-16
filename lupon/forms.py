from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, ValidationError, SubmitField, BooleanField, FloatField, IntegerField, HiddenField, TextField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, URL, Optional
from wtforms.fields.html5 import TelField, DateField

from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import login_required, login_user, current_user, logout_user

from lupon import db
from .models import Contact, User, Location, Task


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
        'E-Mail',
        validators=[
            Email(),
            DataRequired(),
            Length(max=255)
        ],
        render_kw={"placeholder": "e@ma.il", "type": "email"}
    )
    password = PasswordField(
        'Password', 
        validators=[
            DataRequired(),
            Length(max=255)
            ])

    password_repeat = PasswordField(
        'Confirm Password', 
        validators=[
            DataRequired(),
            Length(max=255),
            EqualTo('password',
            message='Passwords must match')
            ])

    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(max=255)
            ], 
        render_kw={"placeholder": "Username"})

    firstname = StringField(
        'Firstname',
        validators=[
            Length(max=255)
            ],
        render_kw={"placeholder": "Firstname"})

    lastname= StringField(
        'Lastname',
        validators=[
            Length(max=255)
            ],
        render_kw={"placeholder": "Lastname"})

    street = StringField(
        'Street',
        validators=[
            Length(max=255)
            ], 
        render_kw={"placeholder": "Street"})

    city = StringField(
        'City',
        validators=[
            Length(max=255)
            ], 
        render_kw={"placeholder": "City"})

    state = StringField(
        'State',
        validators=[
            Length(max=255)
            ],
        render_kw={"placeholder": "State"})

    number = StringField(
        'Street No.',
        validators=[
            Length(max=255)
            ],
        render_kw={"placeholder": "Street No."})

    zip_code = StringField(
        'Zip',
        validators=[
            Length(max=255)
            ], 
        render_kw={"placeholder": "Zip"})

    eula = BooleanField('Accept License Agreement')
    submit = SubmitField('Signup!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first() is not None:
            raise ValidationError(u'This username is already taken')
    
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is not None:
            raise ValidationError(u'This email is already registered')
    
 
class UserProfileForm(FlaskForm):
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname= StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State',validators=[Length(max=255)], render_kw={"placeholder": "State"})
    number = StringField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = StringField('Zip', validators=[Length(max=255)], render_kw={"placeholder": "Zip"})
    submit = SubmitField('Update Profile')

class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class ContactForm(FlaskForm):
    id = HiddenField('id')
    firstname = StringField('Firstname', validators=[Length(max=255)], render_kw={"placeholder": "Firstname"})
    lastname = StringField('Lastname', validators=[Length(max=255)], render_kw={"placeholder": "Lastname"})
    email = StringField('Email', validators=[Email()], render_kw={"placeholder": "Email", "type": "email"})
    phone = TelField('Phone', render_kw={"placeholder": "Phone"})
    mobile = TelField('Mobile', render_kw={"placeholder": "Mobile"})
    fax = StringField('Fax', render_kw={"placeholder": "Fax", "type": "tel"})
    title = StringField('Title', validators=[Length(max=255)], render_kw={"placeholder": "Title"})
    sex = SelectField('Sex', choices=[('n', 'None'),('m', 'Male'),('f', 'Female')], render_kw={"placeholder": "Sex"})
    homepage =  StringField('Homepage', validators=[URL(), Optional()], render_kw={"placeholder": "Homepage"})
    company = StringField('Company', validators=[Length(max=255)], render_kw={"placeholder": "Company"})
    discount =  FloatField('Discount',validators=[Optional(), NumberRange(min=0, max=100)], render_kw={"placeholder": "Discount in %"})
    location = QuerySelectField('Primary Location', allow_blank=True)
    add_contact = SubmitField('Create')
    update_contact = SubmitField('Update')
    del_contact = SubmitField('Delete')

class LocationForm(FlaskForm):
    id = HiddenField('id')
    street = StringField('Street', validators=[Length(max=255)], render_kw={"placeholder": "Street"})
    city = StringField('City', validators=[Length(max=255)], render_kw={"placeholder": "City"})
    state = StringField('State', validators=[Length(max=255)], render_kw={"placeholder": "State"})
    streetNumber = StringField('Street No.', validators=[Length(max=255)], render_kw={"placeholder": "Street No."})
    zip_code = IntegerField('Zip', render_kw={"placeholder": "Zip code"})

class TaskForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Name"})
    amount = FloatField('Amount', render_kw={"placeholder": "Amount"})
    value = FloatField('Value', render_kw={"placeholder": "Value"})
    unit = StringField('Unit', validators=[Length(max=255)], render_kw={"placeholder": "Unit"})
    description = StringField('Description', render_kw={"placeholder": "Description"})
    add_task = SubmitField('Add')
    update_task = SubmitField('Update')
    del_task = SubmitField('Delete')

    #def validate_name(self, field):
    #    if Task.query.filter_by(name=field.data, user_id=current_user.get_id()).first() is not None:
    #        raise ValidationError(u'This name is taken')

class OfferForm(FlaskForm):
    id = HiddenField('id')
    # name = StringField('Name', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Name"})
    name = TextField('Name', render_kw={"placeholder": "Name"})
    location = QuerySelectField('Location', allow_blank=False)
    contact = QuerySelectField('Contact', allow_blank=False)
    add_offer = SubmitField('Add new Offer')


class OfferEditForm(FlaskForm):
    id = HiddenField('id')
    # name = StringField('Name', validators=[DataRequired(), Length(max=255)], render_kw={"placeholder": "Name"})
    name = TextField('Name', render_kw={"placeholder": "Name"})
    location = QuerySelectField('Location', allow_blank=True)
    contact = QuerySelectField('Contact', allow_blank=True)
    discount =  FloatField('Discount',validators=[Optional(), NumberRange(min=0, max=100)], render_kw={"placeholder": "Discount in %"})
    # due_date = DateField('Due Date')
    # start_date = DateField('Start Date')
    task = QuerySelectField('Tasks', allow_blank=False)
    assosiate_task = SubmitField('Add Task to Offer')
    update_offer = SubmitField('Update')
    del_offer = SubmitField('Delete')
