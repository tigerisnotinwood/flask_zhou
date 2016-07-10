# -*- coding:utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from models import db
from views  import login_manager
 
app = Flask(__name__)

# We use Flask-Appconfig here, but this is not a requirement
AppConfig(app)


#BootStrap Settings
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
  
   
#I don't know what is this
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

#Databse Settings
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db.app = app
db.init_app(app)

login_manager.init_app(app)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + 'E:\Web\Python\flask_zhou\app_zhou\date.sqlite'

#db = SQLAlchemy(app)
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#from models.accout import User as db_user


#Blueprint Settings
from views.account import site as account_site
app.register_blueprint(account_site)

from views.quality import site as quality_site
app.register_blueprint(quality_site)

from views.metrology import site as metrology_site
app.register_blueprint(metrology_site)

