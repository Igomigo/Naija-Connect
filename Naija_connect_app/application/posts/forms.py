from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """ Form setup for a new post """
    title = StringField('Title (optional)')
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')