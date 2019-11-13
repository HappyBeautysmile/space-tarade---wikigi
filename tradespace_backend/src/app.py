from flask import Flask
from UsersAPI import users_api
from LoginAPI import login_api
from ItemsAPI import items_api
from SearchAPI import search_api

app = Flask(__name__)
app.register_blueprint(users_api,  url_prefix='/users')
app.register_blueprint(login_api,  url_prefix='/login')
app.register_blueprint(items_api,  url_prefix='/items')
app.register_blueprint(search_api, url_prefix='/search')

@app.route("/")
def hello():
  return "Hello world!"

if __name__ == "__main__":
  app.run()
