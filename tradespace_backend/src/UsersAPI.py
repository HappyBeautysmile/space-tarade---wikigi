from flask import Blueprint
users_api = Blueprint('users_api', __name__)

@users_api.route('/')
def hello():
  return 'Users: Hello World!'

@users_api.route('<user_id>', methods=['GET'])
def get_user(user_id):
  return "USER WITH ID {}".format(user_id)