import pytest

def test_empty_db(client):
  """Checking the hello world route."""
  rv = client.get('/')
  assert b'Hello world' in rv.data
