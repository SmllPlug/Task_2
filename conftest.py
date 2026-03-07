import pytest


from utils import helpers


@pytest.fixture
def created_user():
    payload = helpers.create_user_data()
    response = helpers.create_user(payload)
    access_token = response.json().get('accessToken')
    yield  payload, access_token
    if access_token:
        helpers.delete_user(access_token)

@pytest.fixture
def cleanup_user():
    tokens_to_delete = []
    def register(access_token):
        if access_token is not None:
            tokens_to_delete.append(access_token)
    yield register
    for access_token in tokens_to_delete:
        helpers.delete_user(access_token)