from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from flask_wtf.file import FileField, FileAllowed,file_required


# {#class ContactForm(FlaskForm):
#     fullname = StringField("Fullname",validators=[DataRequired(message="hello, you should supply all your names")])
#     confirm_name = StringField("Confirm Fullname",validators=[DataRequired(message="Haba!"),EqualTo('fullname',message="Do you mean this name is same as the previous?")])
#     email = StringField("Your Email",validators=[Email()])
#     message = TextAreaField("Message", validators=[Length(1,3)])
    
#     btn = SubmitField("Send Message")#}
 
  
class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message=" your fullname is required ")])
   
    email = StringField("Email",validators=[Email()])

    password =PasswordField("Password",validators=[DataRequired()])
    confirm_password =PasswordField("Confirm Password",validators=[EqualTo("password",message="confirm Password must be equal to Password ")])
    
    
    btn = SubmitField("Sign Up!")


class ProfileForm(FlaskForm):
    fullname = StringField("Fullname", validators=[DataRequired(message="Your fullname is required")])

    pix = FileField("Display Picture", validators=[file_required(), FileAllowed(['jpg','png'], 'Images only!')])

    btn = SubmitField("Update Profile")
     
    
    
    
    
     
    

