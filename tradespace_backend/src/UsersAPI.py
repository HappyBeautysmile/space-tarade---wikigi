from flask import Blueprint, jsonify, request, g
from src.TokenAuthentication import auth
import firebase_admin
import sys
from firebase_admin import auth as firebase_auth
from firebase_admin import _auth_utils as firebase_auth_utils
users_api = Blueprint('users_api', __name__)

@users_api.route('/', methods=['GET'])
@auth.login_required
def get_user():
  user_id = g.uid
  user = firebase_auth.get_user(user_id)
  user_data = jsonify(user_id=user_id, display_name=user.display_name, email=user.email, phone_number=user.phone_number, photo_url=user.photo_url)
  return user_data

@users_api.route('/<string:user_id>', methods=['GET'])
@auth.login_required
def get_user_with_id(user_id):
  try:
    user = firebase_auth.get_user(user_id)
    user_data = jsonify(user_id=user_id, display_name=user.display_name, email=user.email, phone_number=user.phone_number, photo_url=user.photo_url)
    return user_data, 200
  except firebase_auth_utils.UserNotFoundError:
    return {'error': 'user id not found'}, 400

@users_api.route('/update/', methods=['POST'])
@auth.login_required
def update_user():
  try:
    data = request.form.to_dict()
    email = data['email']
    display_name = data['display_name']
    phone_number = data['phone_number']
    photo_url = data['photo_url']
    user_id = g.uid
    user = firebase_auth.update_user(user_id, email=email, display_name=display_name, phone_number=phone_number, photo_url=photo_url)
    return  "User Updated", 201
  except firebase_auth_utils.UserNotFoundError:
    return {'error': 'user id not found'}, 400
  except firebase_auth_utils.EmailAlreadyExistsError:
    return {'error': 'email already exists'}, 400
  except firebase_auth_utils.PhoneNumberAlreadyExistsError:
    return {'error': 'phone number already exists'}, 400
  except firebase_auth_utils.UnexpectedResponseError:
    return {'error': 'unexpected response'}, 400
  except:
    print("Unexpected error:", sys.exc_info()[0])
    return {'error': 'request error'}, 400

@users_api.route('/', methods=['POST'])
def create_user():
  try:
    data = request.form.to_dict()
    email = data['email']
    password = data['password']
    display_name = data['display_name']
    phone_number = data['phone_number']
    photo_url = data['photo_url']
    user = firebase_auth.create_user(email=email, password=password, display_name=display_name, phone_number=phone_number, photo_url=photo_url)
    user_data = jsonify(user_id=user.uid)
    return user_data, 201
  except firebase_auth_utils.EmailAlreadyExistsError:
    return {'error': 'email already exists'}, 400
  except firebase_auth_utils.PhoneNumberAlreadyExistsError:
    return {'error': 'phone number already exists'}, 400
  except firebase_auth_utils.UnexpectedResponseError:
    return {'error': 'unexpected response'}, 400
  except:
    print("Unexpected error:", sys.exc_info()[0])
    return {'error': 'request error'}, 400
