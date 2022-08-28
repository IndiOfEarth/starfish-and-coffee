from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    img_link = StringField('Image URL', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    sockets = SelectField("Sockets?", choices=[('yes', 'Has Sockets'), ('no', 'No Sockets')])
    toilets = SelectField("Toilets?", choices=[('yes', 'Has Toilets'), ('no', 'No Toilets')])
    wifi = SelectField("Wifi?", choices=[('yes', 'Has WiFi'), ('no', 'No WiFi')])
    seats = StringField('Number of Seats', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField("Enter")