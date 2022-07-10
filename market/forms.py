from flask_wtf import FlaskForm
from wtforms import StringField

class RegisterForm(FlaskForm):
    username = StringField(Label='username')