from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class nForm(FlaskForm):
    num = IntegerField("Input N", 
        validators=[DataRequired(), NumberRange(min=1, message="N must be > 0")])
    submit = SubmitField("Go!")