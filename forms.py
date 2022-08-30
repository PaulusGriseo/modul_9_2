from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class MyLibrary(FlaskForm):
    author = TextAreaField('Autor', validators=[DataRequired()])
    title = TextAreaField('Tytuł', validators=[DataRequired()])
    year = StringField('Rok', validators=[DataRequired()])
    read = BooleanField('Przeczytane')