import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flssql'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# pagination
POSTS_PER_PAGE = 3

# for request
HEADERS={'Accept': 'application/json'},
USERNAME='user',
PASSWORD='password',
