#user Views
from flask import render_template,url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, login_required , logout_user
from FatigueManagement import db
from werkzeug.security import generate_password_hash,check_password_hash
from FatigueManagement.Models import User, Report
#from FatigueManagement.Users.forms import RegisterationForm, LoginForm, UpdateUserForm
#from FatigueManagement.Users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)

#Registeration
@users.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data,
                    subunit = form.subunit.data,
                    trade = form.trade.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for Registration") # this willl be super quick and may not be read before the return
        return redirect(url_for("users.login"))

    return render_template('register.html', form = form)

#login
@users.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in succesfull!')

            next = request.args.get('next')

            if next == None or not next[0] == "/":
                next = url_for('core.index')
            return redirect(next)
    return render_template("login.html", form = form)

#logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))

#edit Account
@users.route('/account', methods = ['GET', 'POST'])
@login_required

def account():

    form = UpdateUserForm()

    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.trade = form.trade.data
        current_user.subunit = form.subunit.data
        db.session.commit()
        flash(' Account Updated')

    elif request.method == 'GET': #if they arent updating or form doesnt validate, form fields are set to what is already saved
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.trade.data = current_user.trade
        form.subunit.data = current_user.subunit

    return render_template('account.html', profile_image = profile_image, form = form)

#list of user Reports
@users.route('/<username>')
def user_posts(username):
    page = request.args.get('page',1,type=int) #lets you skipp diff error_pages
    user = User.query.filter_by(username = username).first_or_404() # incase name typed manually and was wrong then it can rune the 404 part
    reports = Report.query.filter_by(author = user).order_by(Report.date.desc()).paginate(page=page, per_page =5) #its based on the back ref for the relationship
    return render_template('summary_user.html', reports = reports, user = user)
