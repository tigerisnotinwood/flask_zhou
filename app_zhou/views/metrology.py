from flask import Blueprint, render_template, flash, redirect, url_for, request,g
from flask_login import login_user, logout_user, current_user, login_required
#from ..models import db, NotGoodFuel
from ..decorators import admin_required


site = Blueprint('metrology', __name__)

@site.route('/metrology/')
@login_required
@admin_required
def metrology():
    return render_template('metrology/metrology.html')






