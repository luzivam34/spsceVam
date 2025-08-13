import os

UPLOAD_PATH = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql://postgres:250717@localhost:5432/vamSpace01')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = os.environ.get('FLASK_APP', 'run.py')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']