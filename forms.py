from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class AddItem(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder':'type title'})
    price = IntegerField('Price: ', validators=[DataRequired()], render_kw={'class': 'form-control', 'placeholder':'type price'})
    text = TextAreaField('Text: ', validators=[DataRequired()], render_kw={'class': 'form-control', 'rows': 3, 'placeholder':'type details'})
    submit = SubmitField('Create', render_kw={'class': 'btn btn-outline-primary form-control'})