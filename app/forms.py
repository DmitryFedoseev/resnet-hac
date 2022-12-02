from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('Name class', validators=[DataRequired()])
    file = FileField()
    submit = SubmitField('Submit')