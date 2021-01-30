from flask import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from application import routes
