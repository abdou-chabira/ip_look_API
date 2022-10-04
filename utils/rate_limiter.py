from flask_limiter import Limiter
from flask import request
#from utils.request_info import get_request_ip
from flask_limiter.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)