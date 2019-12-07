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

def login2():
  response = requests.post(
    'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDXj-1A4-KiCMtxbqgkEh6uJnwdN2Bb-40',
    data={
      'email':'test2@test.com',
      'password': 'test@12345',
      'returnSecureToken': True
    })
  json_response = response.json()
  assert 'idToken' in json_response
  return json_response['idToken']

def create_test_item(client, idToken, data):
  # create new item
  rv = client.post(
    '/items/',
    data=data,
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()

  return json_data['item_id']

def delete_test_item(client, idToken, item_id):
  # delete the item
  return client.delete(
    '/items/' + item_id,
    headers={'Authorization': 'token {}'.format(idToken)})

def test_create_trade_success(client):
  idToken = login()

  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  idToken2 = login2()
  rv = client.post(
	'/trades/request_new',
	data={'item_id': test_item_id},
    headers={'Authorization': 'token {}'.format(idToken2)})

  assert rv.status_code == 200

  delete_test_item(client, idToken, test_item_id)

def test_create_trade_fail_invalid_item(client):
  idToken = login()

  rv = client.post(
	'/trades/request_new',
	data={'item_id': 'invalid id'},
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 404

def test_create_trade_fail_not_logged_in(client):
	idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  rv = client.post(
	'/trades/request_new',
	data={'item_id': test_item_id})

  assert rv.status_code == 401

  delete_test_item(client, idToken, test_item_id)

def test_render_trade_success(client):
  idToken = login()

  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  rv = client.post(
	'/trades/request_new',
	data={'item_id': test_item_id},
    headers={'Authorization': 'token {}'.format(idToken)})

  json_data = rv.get_json()
  trade_id = json_data['trade_id']

  rv = client.get(
	'/trades/' + trade_id,
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 200

  delete_test_item(client, idToken, test_item_id)

def test_render_trade_fail_invalid_id(client):
  idToken = login()

  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  rv = client.post(
	'/trades/request_new',
	data={'item_id': test_item_id},
    headers={'Authorization': 'token {}'.format(idToken)})

  rv = client.get(
	'/trades/' + 'invalid id',
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 404

  delete_test_item(client, idToken, test_item_id)

def test_remove_trade_success(client):
  idToken = login()

  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  rv = client.post(
	'/trades/request_new',
	data={'item_id': test_item_id},
    headers={'Authorization': 'token {}'.format(idToken)})

  json_data = rv.get_json()
  trade_id = json_data['trade_id']

  rv = client.post(
	'/trades/' + trade_id + 'remove',
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 200

def test_remove_trade_fail_invalid_id(client):
  idToken = login()

  rv = client.post(
	'/trades/invalidid/remove',
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 404

def test_get_trades_success(client):
  idToken = login()

  rv = client.get(
	'/trades/',
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 200

def test_get_trades_fail_not_logged_in(client):
  rv = client.get(
	'/trades/')

  assert rv.status_code == 401
