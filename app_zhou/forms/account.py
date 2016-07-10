# -*- coding:utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(Form):
    username    = TextField(u'用户名', validators=[Required()])
    password    = TextField(u'密码', validators=[Required()])
    email       = TextField(u'邮箱', validators=[Email()])
    # birthday    = DateField(u'Your birthday')

    # a_float     = FloatField(u'A floating point number')
    # a_decimal   = DecimalField(u'Another floating point number')
    # a_integer   = IntegerField(u'An integer')

    # now         = DateTimeField(u'Current time',
    #                     description='...for no particular reason')
    # sample_file = FileField(u'Your favorite file')
    # eula        = BooleanField(u'I did not read the terms and conditions',
    #                     validators=[Required('You must agree to not agree!')])

    submit      = SubmitField(u'注册')


class loginForm(Form):
    username = StringField(u'账户', validators=[Required()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住账号密码', default = False)

    submit   = SubmitField(u'登录')

    # def validate(self):
    #     print "validateing"
    #     print self.username.data
    #     print self.password.data
    #     if self.username.data == "admin" and self.password.data == "123":
    #         return True
    #     else:
    #         return False
