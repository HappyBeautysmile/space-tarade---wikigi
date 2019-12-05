import pytest

def test_empty_db(client):
  """Checking the hello world route."""
  rv = client.get('/')
  assert b'TradeSpace API is up and running!' in rv.data
