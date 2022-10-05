from flask import jsonify, request
from config.settings import Settings

def api_key_validation(func):
    def inner(*args, **kwargs):
        if request.headers.has_key("Authorization"):
            print("4444444444")
            api_key =Settings.web_api_key()
            header_api_key = request.headers.get("Authorization")[len("Basic "):]
            if api_key == header_api_key:
                returned_value = func(*args, **kwargs) 
                return returned_value
            else:
                return jsonify({"message":"invalid web-api key request", "success":False, "status":401}), 401   
        else:
            return jsonify({"message":" forbidden request", "success":False, "status":403}), 403     
    inner.__name__ =  func.__name__     
    return inner 