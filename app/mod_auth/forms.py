from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(Form):
    email = TextField('Email Address', [
        Email(),
        DataRequired(message='Forgot your email ?')
    ])

    password = PasswordField('Password', [
        DataRequired(message='Must provide a password')
    ])
