from flask import Flask, request,Blueprint
from flask_cors import CORS
from routes.ip_address import ip_address_blueprint
from config.settings import Settings
from utils.rate_limiter import limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__,template_folder="templates")
app.debug = True
CORS(app)
limiter.init_app(app)


API_BASE_PATH = Settings.web_api_url_prefix()
app.register_blueprint(ip_address_blueprint,url_prefix=API_BASE_PATH)
