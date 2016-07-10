# -*- coding:utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,AnonymousUserMixin
from .base import db

class Permission:
    FOLLOW            = 0x01
    COMMENT           = 0x02
    WRITE_ARTICLES    = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER        = 0x80


class Role(db.Model):
    __tablename__ = 'roles'
    id            = db.Column(db.Integer,     primary_key=True)
    name          = db.Column(db.String(64),  unique=True)
    default       = db.Column(db.Boolean, default = False, index = True)
    permissions   = db.Column(db.Integer)
    users         = db.relationship('User', backref = 'role', lazy = 'dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id            = db.Column(db.Integer,     primary_key=True)
    username      = db.Column(db.String(64),  unique=True)
    email         = db.Column(db.String(64),  unique=False)
    password_hash = db.Column(db.String(128), unique=False)
    role_id       = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed     = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('不能直接获取明文密码！')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{:s}>".format(self.username)

    def can(self, permissions):
        return (self.role_id & permissions) == permissions
        #return self.role is not None and (self.role.permissions & permissions) == permissions


    def is_administrator(self):
        return self.can(Permission.ADMINISTER)
