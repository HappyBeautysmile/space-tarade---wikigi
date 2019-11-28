from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from src.UsersAPI import users_api
from src.ItemsAPI import items_api
from src.SearchAPI import search_api
import firebase_admin
from firebase_admin import credentials
from src.TokenAuthentication import auth

# ENTER YOUR FULL LOCAL PATH to the json file here ("/Users/.../tradespace_firebase_admin_key.json") & DON'T COMMIT THE NEXT LINE
cred = credentials.Certificate(
    "/mnt/c/Users/Nikita/Documents/projects/TradeSpace/tradespace_backend/instance/tradespace_firebase_admin_key.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
app.register_blueprint(users_api, url_prefix='/users')
app.register_blueprint(items_api, url_prefix='/items')
app.register_blueprint(search_api, url_prefix='/search')


@app.after_request
def do_something_whenever_a_request_has_been_handled(response):
    # print('headrers')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/authreq")
@auth.login_required
def authreq():
    return "blah"


if __name__ == "__main__":
    app.run()
