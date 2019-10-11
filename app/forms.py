from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Optional
from wtforms.fields.html5 import DateField
from wtforms_alchemy import ModelForm
from app.models import Destination


# Inheriting from FlaskForm gives us hidden_tag() and validate_on_submit()
class DestinationForm(ModelForm, FlaskForm):
    class Meta:
        model = Destination
