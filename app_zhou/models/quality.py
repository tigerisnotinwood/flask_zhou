# -*- coding:utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .base import db


class NotGoodFuel(UserMixin, db.Model):
    __tablename__ = 'not_good_fuel'
    id            = db.Column(db.Integer,     primary_key=True)
    company       = db.Column(db.String(64),  unique=False)
    time_purchase = db.Column(db.String(64),  unique=False)
    fuel_kind     = db.Column(db.String(64),  unique=False)
    quantity      = db.Column(db.Float,       unique=False)
    depot         = db.Column(db.String(64),  unique=False)
    which_no      = db.Column(db.String(64),  unique=False)
    process       = db.Column(db.String(64),  unique=False)
    elseComment   = db.Column(db.String(64),  unique=False)
    #time_created  = 
    #time_modified = 
    def __repr__(self):
        return "<User '{:s}>".format(self.company)