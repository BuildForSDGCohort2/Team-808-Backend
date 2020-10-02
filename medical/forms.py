from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from medical.models import User

class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Laststname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    hospital = StringField('Hospital',
                           validators=[DataRequired(), Length(min=2, max=20)])
    jobname = StringField('Job name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    rmdc = StringField('RMDC Code',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')