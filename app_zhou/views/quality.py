from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from ..forms  import loginForm, SignupForm
from ..models import db, User, NotGoodFuel, Role


site = Blueprint('quality', __name__)

@site.route('/quality/')
def quality():
    notGodFuel = NotGoodFuel.query.all()
    users      = User.query.all()
    roles      = Role.query.all()
    return render_template('quality/quality.html',
                           results = notGodFuel, users = users, roles = roles)






