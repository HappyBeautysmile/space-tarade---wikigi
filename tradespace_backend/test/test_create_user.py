import pytest

def test_success_1(client):
  """Checking the create user route."""
  rv = client.post('/users', data=dict(email='test1234@gmail.com', password='test1234', display_name='test1234', phone_number='+11111111111'), follow_redirects=True)
  assert b'User Created' in rv.data

def test_email_already_exists(client):
  """Checking the create user route."""
  rv = client.post('/users', data=dict(email='test1234@gmail.com', password='test12345', display_name='test12345', phone_number='+12222222222'), follow_redirects=True)
  assert b'{"error":"email already exists"}\n' in rv.data

def test_phone_number_already_exists(client):
  """Checking the create user route."""
  rv = client.post('/users', data=dict(email='test12345@gmail.com', password='test12345', display_name='test12345', phone_number='+11111111111'), follow_redirects=True)
  assert b'{"error":"phone number already exists"}\n' in rv.data

def test_invalid_display_name(client):
  """Checking the create user route."""
  rv = client.post('/users', data=dict(email='test12345@gmail.com', password='test12345', display_name='', phone_number='+12222222222'), follow_redirects=True)
  assert b'{"error":"request error"}\n' in rv.data

def test_success_2(client):
  """Checking the create user route."""
  rv = client.post('/users', data=dict(email='test12345@gmail.com', password='test12345', display_name='test12345', phone_number='+12222222222'), follow_redirects=True)
  assert b'User Created' in rv.data

