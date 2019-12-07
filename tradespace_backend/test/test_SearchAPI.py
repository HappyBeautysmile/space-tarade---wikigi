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

def test_search_success(client):
  idToken = login()

  search_string = 'shoes'
  rv = client.get(
	'/search/' + search_string,
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()

  assert len(json_data) > 0

def test_search_fail_not_logged_in(client):
  search_string = 'shoes'
  rv = client.get(
    '/search/' + search_string)

  assert rv.status_code == 401
