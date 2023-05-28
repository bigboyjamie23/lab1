from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    signup_submit = SubmitField("Sign me up")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    login_submit = SubmitField("Login")
    
