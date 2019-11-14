from flask import Blueprint
from TokenAuthentication import auth
login_api = Blueprint('login_api', __name__)

@login_api.route('/')
@auth.login_required
def hello():
  return 'Login: Hello World!'
