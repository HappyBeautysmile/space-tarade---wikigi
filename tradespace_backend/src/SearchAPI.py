from flask import Blueprint
search_api = Blueprint('search_api', __name__)

@search_api.route('/')
def hello():
  return 'SEARCH: Hello World!'