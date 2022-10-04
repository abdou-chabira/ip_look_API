from flask import jsonify

from config.constants import StatusCode


def success_response(results):
    
    return jsonify({
        "results": results,
        "success": True,
        "status": StatusCode.OK
    }), StatusCode.OK


def error_response(errors, status_code):

    return jsonify({
        "errors": errors,
        "message": errors["message"],
        "success": False,
        "status": status_code
    }), status_code