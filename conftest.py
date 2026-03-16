import pytest


from utils import helpers
from utils import api_methods


@pytest.fixture
def created_user():
    payload = helpers.create_user_data()
    response = api_methods.create_user(payload)
    access_token = response.json().get('accessToken')
    yield  payload, access_token
    if access_token:
        api_methods.delete_user(access_token)

@pytest.fixture
def cleanup_user():
    tokens_to_delete = []
    def register(access_token):
        if access_token is not None:
            tokens_to_delete.append(access_token)
    yield register
    for access_token in tokens_to_delete:
        api_methods.delete_user(access_token)