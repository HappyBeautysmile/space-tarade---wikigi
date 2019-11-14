from flask import Blueprint, request
from TokenAuthentication import auth
import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import _auth_utils as firebase_auth_utils
users_api = Blueprint('users_api', __name__)

@users_api.route('/')
def hello():
  return 'Users: Hello World!'

@users_api.route('<user_id>', methods=['GET'])
def get_user(user_id):
  return "USER WITH ID {}".format(user_id)

@users_api.route('/create_user', methods=['POST'])
def create_user():
  try:
    email = request.form['email']
    password = request.form['password']
    display_name = request.form['display_name']
    phone_number = request.form['phone_number']
    user = firebase_auth.create_user(email=email, password=password, display_name=display_name, phone_number=phone_number)
    return "User Created", 201
  except firebase_auth_utils.EmailAlreadyExistsError:
    return {'error': 'email already exists'}, 400
  except firebase_auth_utils.PhoneNumberAlreadyExistsError:
    return {'error': 'phone number already exists'}, 400
  except firebase_auth_utils.UnexpectedResponseError:
    return {'error': 'unexpected response'}, 400
  except:
    return {'error': 'request error'}, 400
