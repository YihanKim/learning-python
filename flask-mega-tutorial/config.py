import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # session key generator
    SECRET_KEY = os.environ.get('SECRET_KEY') or "d3v3l0p3r5.vun0.c0"

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

