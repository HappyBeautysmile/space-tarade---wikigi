import pytest

# def test_success_1(client):
#   rv = client.post('/users', data=dict(email='test1234@gmail.com', password='test1234', display_name='test1234', phone_number='+11111111111', photo_url='gs://tradespace-22f37.appspot.com/user1/profile.jpg'), follow_redirects=True)
#   print(rv.data)
#   assert b'User Created' in rv.data

# def test_email_already_exists(client):
#   rv = client.post('/users', data=dict(email='test1234@gmail.com', password='test12345', display_name='test12345', phone_number='+12222222222', photo_url='gs://tradespace-22f37.appspot.com/user1/profile.jpg'), follow_redirects=True)
#   assert b'{"error":"email already exists"}\n' in rv.data

# def test_phone_number_already_exists(client):
#   rv = client.post('/users', data=dict(email='test12345@gmail.com', password='test12345', display_name='test12345', phone_number='+11111111111', photo_url='gs://tradespace-22f37.appspot.com/user1/profile.jpg'), follow_redirects=True)
#   assert b'{"error":"phone number already exists"}\n' in rv.data

# def test_invalid_display_name(client):
#   rv = client.post('/users', data=dict(email='test12345@gmail.com', password='test12345', display_name='', phone_number='+12222222222', photo_url='gs://tradespace-22f37.appspot.com/user2/profile.jpg'), follow_redirects=True)
#   assert b'{"error":"request error"}\n' in rv.data

# def test_success_2(client):
#   rv = client.post('/users', data=dict(email='test12345@gmail.com', password='test12345', display_name='test12345', phone_number='+12222222222', photo_url='gs://tradespace-22f37.appspot.com/user2/profile.jpg'), follow_redirects=True)
#   assert b'User Created' in rv.data
