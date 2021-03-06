#project __Init__

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fatigue'

############## Database Setup

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

######## Setup LOGIN Confiurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

################# LINKS TO VIEWS
#links to the core views
from FatigueManagement.Core.views import core
app.register_blueprint(core)

#links to the error pages views
from FatigueManagement.Error_Pages.handlers import error_pages
app.register_blueprint(error_pages)

# Link with user VIEWS
from FatigueManagement.Users.views import users
app.register_blueprint(users)

from FatigueManagement.Assessment_Report.views import reports
app.register_blueprint(reports)
