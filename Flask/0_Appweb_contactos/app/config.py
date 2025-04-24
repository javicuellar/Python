import os



SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
DEBUG = True
PWD = os.path.abspath(os.curdir)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False

