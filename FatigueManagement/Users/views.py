#user Views
from flask import render_template,url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, login_required , logout_user
from FatigueManagement import db
from werkzeug.security import generate_password_hash,check_password_hash
from FatigueManagement.Models import User, Report
#from FatigueManagement.Users.forms import RegisterationForm, LoginForm, UpdateUserForm
#from FatigueManagement.Users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)
