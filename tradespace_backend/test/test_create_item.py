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

def test_success_1(client):
  idToken = login()
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

def test_fails_if_not_logged_in(client):
  rv = client.post(
    '/items/',
    data={
      'title': 'Herschel Backpack',
      'location': 'Los Angeles',
      'description': 'Great for college!',
      'tags': ['backpacks', 'trendy'],
    })
  assert rv.status_code == 401

def test_400s_if_missing_required_param(client):
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