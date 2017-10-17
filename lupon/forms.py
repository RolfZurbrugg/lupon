from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.fields import FormField

from lupon import db
from lupon.models import Contact
BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session

class ContactForm(ModelForm):
    class Meta:
        model = Contact

'''
class UserForm(ModelForm):
    class Meta:
        model = User


class LocationForm(ModelForm):
    class Meta:
        model = Location

class CompanyForm(ModelForm):
    class Meta:
        model = Company


class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class AddCustomerForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
'''
