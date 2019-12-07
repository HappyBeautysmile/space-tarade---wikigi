import pytest
import requests

def login():
  response = requests.post(
    'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDXj-1A4-KiCMtxbqgkEh6uJnwdN2Bb-40',
    data={
      'email':'test1@test.com',
      'password': 'test@12345',
      'returnSecureToken': True
    })
  json_response = response.json()
  assert 'idToken' in json_response
  return json_response['idToken']

def test_create_user_success(client):
  # create new user
  data = {
	'email': 'test@tradespace.com',
	'password': 'password',
	'display_name': 'test user',
	'phone_number': '+21111111111',
	'photo_url': 'https://firebasestorage.googleapis.com/v0/b/tradespace-22f37.appspot.com/o/6SfUOCvdTCMhJqSa10tSHuEHrC72%2Fprofile.jpg?alt=media&token=26471a30-67d2-47ff-bf2c-c1eebde661bf'
  }
  rv = client.post(
    '/users/',
    data=data)
  json_data = rv.get_json()

  user_id = json_data['user_id']
  assert len(user_id) > 0

  # delete the user
  rv = client.delete(
    '/users/' + user_id)

def test_create_user_fail_email_already_exists(client):
  # create new user
  data = {
	'email': 'test@tradespace.com',
	'password': 'password',
	'display_name': 'test user',
	'phone_number': '+11111111111',
	'photo_url': 'https://firebasestorage.googleapis.com/v0/b/tradespace-22f37.appspot.com/o/6SfUOCvdTCMhJqSa10tSHuEHrC72%2Fprofile.jpg?alt=media&token=26471a30-67d2-47ff-bf2c-c1eebde661bf'
  }
  rv = client.post(
    '/users/',
    data=data)
  json_data = rv.get_json()

  # create another user with the same information
  rv = client.post(
    '/users/',
    data=data)

  assert rv.status_code == 400

  print(json_data)
  user_id = json_data['user_id']

  # delete the user
  rv = client.delete(
    '/users/' + user_id)

def test_get_user_success(client):
  idToken = login()

  # get user
  rv = client.get(
    '/users/',
    headers={'Authorization': 'token {}'.format(idToken)})
  assert rv.status_code == 200


def test_get_user_with_id_success(client):
  idToken = login()
  # create new user
  data = {
	'email': 'test@tradespace.com',
	'password': 'password',
	'display_name': 'test user',
	'phone_number': '+11111111111',
	'photo_url': 'https://firebasestorage.googleapis.com/v0/b/tradespace-22f37.appspot.com/o/6SfUOCvdTCMhJqSa10tSHuEHrC72%2Fprofile.jpg?alt=media&token=26471a30-67d2-47ff-bf2c-c1eebde661bf'
  }
  rv = client.post(
    '/users/',
    data=data,
    headers={'Authorization': 'token {}'.format(idToken)})

  json_data = rv.get_json()
  user_id = json_data['user_id']

  # get user
  rv = client.get(
    '/users/' + user_id,
    headers={'Authorization': 'token {}'.format(idToken)})

  json_data = rv.get_json()
  assert json_data['email'] == data['email']
  assert json_data['password'] == data['password']
  assert json_data['display_name'] == data['display_name']
  assert json_data['phone_number'] == data['phone_number']

  # delete the user
  rv = client.delete(
    '/users/' + user_id)

def test_get_user_with_id_fail_invalid_id(client):
  idToken = login()
  # get user with fake id
  rv = client.get(
    '/users/' + "fakeid",
    headers={'Authorization': 'token {}'.format(idToken)})
  assert rv.status_code == 400

def test_update_user_success(client):
  idToken = login()

  # create new user
  data = {
	'email': 'test@tradespace.com',
	'password': 'password',
	'display_name': 'test user',
	'phone_number': '+11111111111',
	'photo_url': 'https://firebasestorage.googleapis.com/v0/b/tradespace-22f37.appspot.com/o/6SfUOCvdTCMhJqSa10tSHuEHrC72%2Fprofile.jpg?alt=media&token=26471a30-67d2-47ff-bf2c-c1eebde661bf'
  }
  rv = client.post(
    '/users/',
    data=data,
    headers={'Authorization': 'token {}'.format(idToken)})

  new_data = {
	'email': 'testEDITED@tradespace.com',
	'password': 'passwordEDITED',
	'display_name': 'test user EDITED',
	'phone_number': '+11111111111',
	'photo_url': 'https://firebasestorage.googleapis.com/v0/b/tradespace-22f37.appspot.com/o/6SfUOCvdTCMhJqSa10tSHuEHrC72%2Fprofile.jpg?alt=media&token=26471a30-67d2-47ff-bf2c-c1eebde661bf'
  }
  rv = client.post(
    '/users/update',
    data=data)

  assert rv.status_code == 201

  # delete the user
  rv = client.delete(
    '/users/' + user_id)
