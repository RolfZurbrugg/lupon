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

class UserCreateForm(ModelForm):
    class Meta:
        model = User
        login = TextField
        
        
        email = TextField(
            validators=[
                Email(),
                DataRequired(),
                Length(max=255)
            ]
        )
        password = PasswordField(
            validators=[
                DataRequired(),
                Length(max=255, min=6)
            ]
        ),
        username = TextField(
            validators=[
                DataRequired(),
                Length(max=255, min=6)
            ]
        ),