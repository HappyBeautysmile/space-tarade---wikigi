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

def test_success_without_uid(client):
  idToken = login()
  rv = client.get(
    '/users/',
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()
  assert json_data['display_name'] == 'Test One'
  assert json_data['email'] == 'test1@test.com'
  assert json_data['phone_number'] == '+11111111111'
  assert json_data['photo_url'] == 'gs://tradespace-22f37.appspot.com/FsRLKnZCAQUne6fw7VbxkOLDHRw1/profile.jpg'

def test_success_with_uid(client):
  idToken = login()
  rv = client.get(
    '/users/EPvxkRaIV8YnblrYaU0GNr61Krn2',
    headers={'Authorization': 'token {}'.format(idToken)})
  json_data = rv.get_json()
  assert json_data['email'] == 'test2@test.com'
