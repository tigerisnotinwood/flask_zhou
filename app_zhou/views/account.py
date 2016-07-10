# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from flask import Blueprint, render_template, flash, redirect, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from ..forms import loginForm, SignupForm
from ..models import db, User


site = Blueprint('account', __name__)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'account.login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@site.before_request
def before_request():
    print before_request.__name__
    print current_user
    g.user = current_user

@site.route('/')
@site.route('/index')
@login_required
def index():
    print index.__name__
    #print current_user
    return render_template('index.html')


#User Login View
@site.route('/login/', methods=('GET', 'POST'))
def login():
    print login.__name__
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        print user
        if user is not None:
            login_user(user)
            next_URL = request.args.get('next').encode('utf-8').replace('/','')
            return redirect(url_for('account.index'))
            #return redirect(url_for(next_URL) or url_for('account.index'))
        else:
            print "shit"


    return render_template('login.html', form=form)

       
@site.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('account.index'))


#User Register View
@site.route('/signup/', methods=('GET', 'POST'))
def Signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user is None:
            user = User(username = form.username.data,
             password = form.password.data,
             email = form.email.data)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('account.index'))
        else:
            flash(user.username + "is already exists")

    return render_template('signup/signup.html', form = form)



