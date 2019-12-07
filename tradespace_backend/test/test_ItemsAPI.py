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

def test_create_item_success(client):
  idToken = login()
  # create new item
  rv = client.post(
    '/items/',
    data={
      'title': 'Herschel Backpack',
      'location': 'Los Angeles',
      'description': 'Great for college!',
      'tags': ['backpacks', 'trendy'],
    },
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()
  assert json_data['title'] == 'Herschel Backpack'
  assert json_data['location'] == 'Los Angeles'

  item_id = json_data['item_id']
  # delete the item
  rv = client.delete(
    '/items/' + item_id,
    headers={'Authorization': 'token {}'.format(idToken)})

def test_create_item_fail_not_logged_in(client):
  rv = client.post(
    '/items/',
    data={
      'title': 'Herschel Backpack',
      'location': 'Los Angeles',
      'description': 'Great for college!',
      'tags': ['backpacks', 'trendy'],
    })
  assert rv.status_code == 401

def test_create_item_fail_missing_required_param(client):
  idToken = login()
  rv = client.post(
    '/items/',
    data={
      'title': 'Herschel Backpack',
      'description': 'Great for college!',
      'tags': ['backpacks', 'trendy'],
    },
    headers={'Authorization': 'token {}'.format(idToken)})
  assert rv.status_code == 400
  assert b'missing required params' in rv.data

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

def test_get_item_success(client):
  idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  # get item
  rv = client.get(
    '/items/' + test_item_id,
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()
  assert json_data['title'] == 'Herschel Backpack'
  assert json_data['location'] == 'Los Angeles'

  delete_test_item(client, idToken, test_item_id)

def test_get_item_fail_invalid_id(client):
  idToken = login()

  # get item
  rv = client.get(
    '/items/' + 'fakeid',
    headers={'Authorization': 'token {}'.format(idToken)})
  assert rv.status_code == 404

def test_get_item_fail_not_logged_in(client):
  idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  # get item without passing authToken
  rv = client.get(
    '/items/' + 'fakeid')
  assert rv.status_code == 401

  delete_test_item(client, idToken, test_item_id)

def test_update_item_success(client):
  idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  # update item
  new_data = {
    'title': 'Herschel Backpack EDITED',
    'location': 'Los Angeles EDITED',
    'description': 'Great for college! EDITED',
    'tags': ['backpacks', 'trendy'],
  }
  rv = client.put(
    '/items/' + test_item_id,
	data=new_data,
    headers={'Authorization': 'token {}'.format(idToken)})

  json_data = rv.get_json()
  assert json_data['title'] == 'Herschel Backpack EDITED'
  assert json_data['location'] == 'Los Angeles EDITED'
  assert json_data['description'] == 'Great for college! EDITED'

  delete_test_item(client, idToken, test_item_id)

def test_update_item_fail_invalid_id(client):
  idToken = login()

  # update item with invalid id
  new_data = {
    'title': 'Herschel Backpack EDITED',
    'location': 'Los Angeles EDITED',
    'description': 'Great for college! EDITED',
    'tags': ['backpacks', 'trendy'],
  }
  rv = client.put(
    '/items/' + "fakeid",
	data=new_data,
    headers={'Authorization': 'token {}'.format(idToken)})

  assert rv.status_code == 404

def test_update_item_fail_not_logged_in(client):
  idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  # update item without passing idToken
  new_data = {
    'title': 'Herschel Backpack EDITED',
    'location': 'Los Angeles EDITED',
    'description': 'Great for college! EDITED',
    'tags': ['backpacks', 'trendy'],
  }
  rv = client.put(
    '/items/' + test_item_id,
	data=new_data)

  assert rv.status_code == 401

  delete_test_item(client, idToken, test_item_id)

def test_delete_item_fail_invalid_id(client):
  idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  # delete item with invalid id
  rv = delete_test_item(client, idToken, "fakeid")

  assert rv.status_code == 404

  delete_test_item(client, idToken, test_item_id)

def test_delete_item_fail_not_logged_in(client):
  idToken = login()
  data = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_id = create_test_item(client, idToken, data)

  rv = delete_test_item(client, "faketoken", test_item_id)
  assert rv.status_code == 401

  delete_test_item(client, idToken, test_item_id)

def test_get_items_success(client):
  idToken = login()
  data1 = {
    'title': 'Herschel Backpack',
    'location': 'Los Angeles',
    'description': 'Great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  data2 = {
    'title': 'Another Backpack',
    'location': 'Santa Monica',
    'description': 'Also great for college!',
    'tags': ['backpacks', 'trendy'],
  }
  test_item_ids = []
  test_item_ids.append(create_test_item(client, idToken, data1))
  test_item_ids.append(create_test_item(client, idToken, data2))

  # get items
  rv = client.get(
    '/items/',
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()

  assert len(json_data) == 2

  for id in test_item_ids:
    rv = delete_test_item(client, idToken, id)
