from flask import Flask

from flask_mail import Mail,Message

from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

from flask_wtf.csrf import CSRFProtect



app=Flask(__name__,template_folder='templates',static_folder='static',instance_relative_config=True)
csrf=CSRFProtect(app)
mail=Mail(app)

app.config.from_pyfile('config.py')

db=SQLAlchemy(app)

migrate=Migrate(app, db)

from p_package import views, models,api