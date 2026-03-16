import allure


from utils import helpers
from utils import api_methods
from utils import data


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя')
    def test_create_user_with_valid_data(self, cleanup_user):
        user_data = helpers.create_user_data()
        response = api_methods.create_user(user_data)
        response_data = response.json()
        access_token = response_data.get('accessToken')
        cleanup_user(access_token)
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка создания уже зарегистрированного пользователя')
    def test_create_user_with_existing_user(self, created_user):
        payload, _ = created_user
        response = api_methods.create_user(payload)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data.get('message') == data.MESSAGE_USER_ALREADY_EXISTS

    @allure.title('Проверка создания пользователя без email')
    def test_create_user_without_email(self):
        payload = helpers.create_user_data_without_email()
        response = api_methods.create_user(payload)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data.get('message') == data.MESSAGE_REQUIRED_FIELDS

    @allure.title('Проверка создания пользователя без password')
    def test_create_user_without_password(self):
        payload = helpers.create_user_data_without_password()
        response = api_methods.create_user(payload)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data.get('message') == data.MESSAGE_REQUIRED_FIELDS

    @allure.title('Проверка создания пользователя без name')
    def test_create_user_without_name(self):
        payload = helpers.create_user_data_without_name()
        response = api_methods.create_user(payload)
        response_data = response.json()
        assert response.status_code == 403
        assert response_data.get('message') == data.MESSAGE_REQUIRED_FIELDS