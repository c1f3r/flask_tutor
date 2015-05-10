from __future__ import unicode_literals
import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:ak3nat3r@localhost:3306/microblog'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
