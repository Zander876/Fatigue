#user forms

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed # allows to update png or jpg file

from flask_login import current_user
from FatigueManagement.Models import User

# Registration
class RegisterationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    subunit = StringField('Subunit', validators = [DataRequired()])
    trade = StringField('Trade', validators = [DataRequired()])
    password =PasswordField('Password', validators= [DataRequired()])
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('This email has already been registered! Please use a different email.')

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('This username has already been registered! Please use a different username.')


# Login
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password =PasswordField('Password', validators= [DataRequired()])
    submit = SubmitField('Login')


# Updates
class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators = [Email()])
    username = StringField('Username')
    trade = StringField('Trade')
    subunit = StringField('Subunit')
    password =PasswordField('Password')
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('This email has already been registered! Please use a different email.')

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('This username has already been registered! Please use a different username.')
