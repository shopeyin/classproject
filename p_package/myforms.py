""" this module contains classes for my webform """
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email


class ContactForm(FlaskForm):
    """ the contact us form"""
    name = StringField("Name: ",validators=[DataRequired(message='input')])
    email = StringField("Email: ",validators=[Email(message='WTF!!!')])
    message= TextAreaField("Message",validators =[DataRequired()])
    submit = SubmitField("Submit") 

class LoginForm(FlaskForm):
    """ the contact us form"""
    username = StringField("UserName: ",validators=[DataRequired(message='input'),Email()])
    password = PasswordField("Password: ",validators=[DataRequired(message='WTF!!!')])
    submit = SubmitField("Login") 


class SignUp(FlaskForm):
    """sign up form"""
    username = StringField("UserName: ",validators=[DataRequired(message='input'),Email()])
    email = StringField("Email: ", validators=[Email(message='what')])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit= SubmitField("SignUp")



class Usersignup(FlaskForm):
    """signing up"""
    passport = FileField('Upload passport', validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'],'images only')])
    firstname = StringField("UserName: ",validators=[DataRequired(message='input')])
    lastname = StringField("Lastname: ",validators=[DataRequired(message='input')])
    email = StringField("Email: ",validators=[Email(message='WTF!!!')])
    password = PasswordField("Password: ",validators=[DataRequired(message='WTF!!!')])
   
    submit= SubmitField("Sign up now")

class Register(FlaskForm):
    """register"""
    username = StringField("USERNAME :", validators=[DataRequired(message='input')])
    password = PasswordField("Password: ",validators=[DataRequired(message='input')])
    register = SubmitField("REGISTER")


class Payment(FlaskForm):
    custname = StringField("Customer Fullname: ", validators=[DataRequired(message='Pls fill this field')])
    email = StringField("Email: ", validators=[DataRequired(message='Pls fill this field'),Email()])
    phone = StringField("Phone: ", validators=[DataRequired(message='Pls fill this field')])
    submit = SubmitField("Make Payment")


