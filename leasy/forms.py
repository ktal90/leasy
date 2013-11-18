# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(Form):
    firstname = TextField('First name', validators=[DataRequired(), Length(min=2, max=25)])
    lastname = TextField('Last name', validators=[DataRequired(), Length(min=2, max=25)])
    email = TextField('Email', validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                                validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField(
                'Verify password',
                [DataRequired(), EqualTo('password', message='Passwords must match')])

class LoginForm(Form):
    email = TextField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])