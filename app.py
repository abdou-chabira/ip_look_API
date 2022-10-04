from flask import Flask, request,Blueprint
from flask_cors import CORS
#from celery import Celery

app = Flask(__name__,template_folder="templates")
app.debug = True
CORS(app)

app.register_blueprint()