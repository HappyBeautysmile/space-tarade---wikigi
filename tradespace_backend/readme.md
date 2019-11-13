# The Tradespace Backend

This is a flask app that will wrap our calls to firebase and expose a RESTful API to our web client.
The `src` directory contains the code for the app. The `test` directory contains tests.

# Instructions for running the server (locally)
These instructions work only for MacOS. Please look up virtualenv docs for Windows if you need to.
1. Make sure you have the correct python version (Python 3.6) installed on your laptop.
2. Make sure you have `virtualenv` installed on your machine.
  ```
  pip install --user virtualenv
  ```
2. Create a virtual environment on your local machine, by running the following commands:
  ```
  virtualenv --python=/usr/local/bin/python3.6 .env
  ```
  NOTE: the path `/usr/local/bin/python3.6` is usually where MacOS installs python.
3. Activate your virtual environment
  ```
  source .env/bin/activate
  ```
4. Install the required packages
  ```
  pip install -r requirements.txt
  ```
5. Enter the `src` directory
  ```
  cd src
  ```
6. Run the server!
  ```
  flask run
  ```
7. Server should be running on http://localhost:5000

This setup is required just once. Every subsequent time you should only need to activate the virtual env (step 3), and run the server from the `src` folder (steps 5 & 6). If `requirements.txt` gets updated (which will happen if add/remove dependencies) then you should repeat step 4 too.

# Adding endpoints
As you can see, the setup for each of the top-level routes has already been done in `app.py`. In the current state, if you visit `localhost:5000/users/`, `localhost:5000/login/`, etc you should see some hello world messages. I have used [Flask Blueprints](https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files) to "modularize" our API code so each API can live in a separate file.

Now, if you wanted to add an endpoint say `GET /users/<task_id>`, you could just add the following code in the `UserAPI.py` file.
```
@users_api.route('<user_id>', methods=['GET'])
def get_user(user_id):
  return "USER WITH ID {}".format(user_id)
```

This is similar across the different top-level routes. For more info on how to define different kinds of requests and how to do cool stuff like using part of the URL (`<user_id>`) as a param, I would just look up some flask examples or docs.

# Authentication
* Initial investigation suggests `flask-httpauth` is a good package to use (will need to be pip installed)
* Can use the **Token Authentication Scheme** from this article: https://flask-httpauth.readthedocs.io/en/latest/

# Adding tests
Haven't looked into this too much yet. Here is a doc I found that might come in handy:
* https://flask.palletsprojects.com/en/1.1.x/testing/
