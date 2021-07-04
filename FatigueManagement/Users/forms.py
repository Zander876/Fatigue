#user forms

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed # allows to update png or jpg file

from flask_login import current_user
from FatigueManagement.Models import User

# Registration
class RegisterationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    subunit = SelectField('Subunit', validators = [DataRequired()], choices=[('1flt','No 1 Flt'), ('2flt','No 2 Flt'), ('1fd','1 Fd Wksp'), ('sp','Sp Flt')])
    trade = RadioField('Trade', validators = [DataRequired()], choices=[('pilot','Pilot'),('crewman','Aircrewman'),('esop','Sensor Operator'),('tech','Technician'),('atc','Air Traffic Controller'),('fire','Fireman')])
    password =PasswordField('Password', validators= [DataRequired()])
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('This email has already been registered! Please use a different email.')

    def check_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('This username has already been registered! Please use a different username.')

    #def password_check(self,field):


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
