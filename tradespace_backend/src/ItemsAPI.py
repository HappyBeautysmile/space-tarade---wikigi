from flask import Blueprint
items_api = Blueprint('items_api', __name__)

@items_api.route('/')
def hello():
  return 'Items: Hello World!'