from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email


class WriteArticle(FlaskForm):
    title = StringField('Title', [
        DataRequired(message='Title is required')
    ])

    content = TextAreaField('Content', [
        DataRequired(message='Content is required')
    ])
