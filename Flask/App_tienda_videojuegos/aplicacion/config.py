import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:{}@{}/tienda'.format(os.environ["MYSQL_PASSWORD"],os.environ["MYSQL_PORT_3306_TCP_ADDR"])
SQLALCHEMY_TRACK_MODIFICATIONS = False

