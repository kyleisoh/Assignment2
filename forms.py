from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    item_name = StringField("name", validators=[DataRequired()])