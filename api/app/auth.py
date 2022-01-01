from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.models import User
from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
#from app.errors import error_response


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user

@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)

@token_auth.verify_token
def verify_token(token):
    return User.check_token(token) if token else None

@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)