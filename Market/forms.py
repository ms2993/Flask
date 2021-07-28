from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired

class Registrationform(FlaskForm):
    username = StringField(label = 'User Name:', validators= [Length(min=3, max=10),DataRequired()])
    email = StringField(label = 'Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label = 'Password:', validators=[DataRequired()])
    password2 = PasswordField(label= 'Confirm Password:')
    submit = SubmitField(label= 'Submit')