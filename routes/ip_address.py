from crypt import methods
from flask import Flask, Blueprint,request
from services.data_validation.validate_data import validate_ip_address,validate_ip_abuse
from services.ip_address_service import lookup_ip_address,save_report_ip_abuse
from utils.responses import error_response,success_response
from config.constants import StatusCode
from utils.api_key_validation import api_key_validation
from utils.rate_limiter import limiter
from db.ip_address_db import get_abuse_by_ip
ip_address_blueprint = Blueprint('ip_address_blueprint', __name__)


@ip_address_blueprint.route("/ip-address/<ip_addr>",methods=["GET"])
def get_ip_address_info(ip_addr):
    if not validate_ip_address(ip_addr):
        return error_response({"message":"invalid ip address"},StatusCode.BAD_REQUEST)
    ip_addr_jdata=lookup_ip_address(ip_addr)
    print(ip_addr_jdata)
    return success_response(ip_addr_jdata)


@ip_address_blueprint.route("/ip-address/abuse",methods=["POST"])
@api_key_validation
def report_ip_abuse():
    abuse_jdata = request.get_json()
    try:
        if not validate_ip_abuse(abuse_jdata):
            return error_response({"message":"bad data"},StatusCode.BAD_REQUEST)
        abuse_report_data=save_report_ip_abuse(abuse_jdata)
        return success_response(abuse_report_data)
    except ValueError:
        return error_response({"message":"bad data"},StatusCode.INTERNAL_SERVER_ERROR)


@ip_address_blueprint.route("/ip-address/abuse/<ip_addr>",methods=["GET"])
@limiter.limit("10/second",override_defaults=False)
def get_all_ip_abuse(ip_addr):
    category=""
    if not validate_ip_address(ip_addr):
        return error_response({"message":"bad data"},StatusCode.BAD_REQUEST)
    if "category" in request.args:
        category=request.args.get("category")
    resp=get_abuse_by_ip(ip_addr,category)
    return success_response(resp)
    

