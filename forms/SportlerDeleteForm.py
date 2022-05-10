from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField, SelectField
from wtforms import validators

class SportlerDeleteForm(FlaskForm):
    Sportler_ID = StringField("Sportler_ID",[validators.InputRequired()])