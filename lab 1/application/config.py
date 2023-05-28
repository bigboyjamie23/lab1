import os
from application import app

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'secrfgdgret'