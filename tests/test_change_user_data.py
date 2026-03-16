import allure


from utils import helpers
from utils import api_methods
from utils import data


class TestChangeUserData:
    @allure.title('Проверка смены email у авторизованного пользователя')
    def test_change_email_authorized_user(self, created_user):
        payload, access_token = created_user
        new_payload = {
            'email': payload['email'] + 'new',
            'name': payload['name'],
            'password': payload['password']
        }
        response = api_methods.change_user_data(new_payload, access_token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка смены email на уже существующий у авторизованного пользователя')
    def test_change_email_to_exists_email_authorized_user(self, cleanup_user):
        first_user = helpers.create_user_data()
        first_response = api_methods.create_user(first_user)
        first_access_token = first_response.json().get('accessToken')
        cleanup_user(first_access_token)
        second_user = helpers.create_user_data()
        second_response = api_methods.create_user(second_user)
        second_access_token = second_response.json().get('accessToken')
        cleanup_user(second_access_token)
        new_payload = {
            'email': first_user['email'],
            'name': second_user['name'],
            'password': second_user['password']
        }
        response = api_methods.change_user_data(new_payload, second_access_token)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data.get('message') == data.MESSAGE_USER_EMAIL_EXISTS

    @allure.title('Проверка смены password у авторизованного пользователя')
    def test_change_password_authorized_user(self, created_user):
        payload, access_token = created_user
        new_payload = {
            'email': payload['email'],
            'name': payload['name'],
            'password': payload['password'] + 'new'
        }
        response = api_methods.change_user_data(new_payload, access_token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка смены name у авторизованного пользователя')
    def test_change_name_authorized_user(self, created_user):
        payload, access_token = created_user
        new_payload = {
            'email': payload['email'],
            'name': payload['name'] + 'new',
            'password': payload['password']
        }
        response = api_methods.change_user_data(new_payload, access_token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка смены email у неавторизованного пользователя')
    def test_change_email_unauthorized_user(self):
        new_payload = {
            'email': 'newemail@test.ru'
        }
        response = api_methods.change_user_data(new_payload)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data.get('message') == data.MESSAGE_UNAUTHORIZED

    @allure.title('Проверка смены password у неавторизованного пользователя')
    def test_change_password_unauthorized_user(self):
        new_payload = {
            'password': 'newpassword'
        }
        response = api_methods.change_user_data(new_payload)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data.get('message') == data.MESSAGE_UNAUTHORIZED

    @allure.title('Проверка смены name у неавторизованного пользователя')
    def test_change_name_unauthorized_user(self):
        new_payload = {
            'name': 'newname'
        }
        response = api_methods.change_user_data(new_payload)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data.get('message') == data.MESSAGE_UNAUTHORIZED