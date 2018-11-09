import os

import pytest

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_get(client):
  rv = client.get('/')
  assert b'<p>Hello, World</p>' in rv.data


def test_get_header(client):
  rv = client.get('/', headers={'Accept': 'application/json'})
  assert b'{"message":"Good morning"}\n' in rv.data
