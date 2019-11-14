from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from UsersAPI import users_api
from LoginAPI import login_api
from ItemsAPI import items_api
from SearchAPI import search_api
import firebase_admin
from firebase_admin import credentials
from TokenAuthentication import auth

cred = credentials.Certificate("../instance/tradespace_firebase_admin_key.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
app.register_blueprint(users_api,  url_prefix='/users')
app.register_blueprint(login_api,  url_prefix='/login')
app.register_blueprint(items_api,  url_prefix='/items')
app.register_blueprint(search_api, url_prefix='/search')

@app.route("/")
def hello():
  return "Hello world!"

@app.route("/authreq")
@auth.login_required
def authreq():
    return "blah"

if __name__ == "__main__":
  app.run()
