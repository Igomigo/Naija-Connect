""" This module contains code that handles the registration
    and login operations for the app
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User


class RegistrationForm(FlaskForm):
    """ Creates the registration form with all required fields and data"""
    username = StringField("Username", 
                          validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    state = StringField("State of Origin", validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        """ Function that validates the username input on submit from the form
            and checks to ensure that the name doesn't already exist 
            in the database.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist. Please choose a different one.')
        
    def validate_email(self, email):
        """
            Function that validates the email input on submit from the form
            and checks to ensure that the email doesn't already exist 
            in the database.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist. Please choose a different one.')

class LoginForm(FlaskForm):
    """ Creates the login form with all required fields and data"""
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class UpdateAcountForm(FlaskForm):
    """ Creates the update account form with all required fields and data"""
    username = StringField("Username", 
                          validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    state = StringField("State", validators=[DataRequired()])
    bio = TextAreaField("Bio")
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_username(self, username):
        """ Function that validates the username input on submit from the form
            and checks to ensure that the name doesn't already exist 
            in the database.
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exist. Please choose a different one.')
        
    def validate_email(self, email):
        """
            Function that validates the email input on submit from the form
            and checks to ensure that the email doesn't already exist 
            in the database.
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exist. Please choose a different one.')
            

class RequestResetForm(FlaskForm):
    """ Reset Password Form """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email, you must register first.')
        

class ResetPasswordForm(FlaskForm):
    """ Reset password form setup """
    password = PasswordField('Enter New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')