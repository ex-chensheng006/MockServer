import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

USERNAME = 'root'
PASSWORD = '@Welcome#Sicent110'
HOST = '10.34.57.131:3306'
DB = 'MockServer'

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://%s:%s@%s/%s' % (USERNAME, PASSWORD, HOST, DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
