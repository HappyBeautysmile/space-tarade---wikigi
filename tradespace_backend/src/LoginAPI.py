from flask import Blueprint
login_api = Blueprint('login_api', __name__)

@login_api.route('/')
def hello():
  return 'Login: Hello World!'