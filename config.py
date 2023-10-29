import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OIDC_CLIENT_ID = "base-image-reconciler"
    OIDC_CLIENT_SECRET = "8iDcaxWIVGS2rYluuhKfH1VLT2dijVWP"
