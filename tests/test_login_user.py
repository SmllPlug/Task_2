import allure


from utils import api_methods
from utils import data


class TestLoginUser:
    @allure.title('Проверка логина существующего пользователя')
    def test_login_user_with_existing_user(self, created_user):
        payload, _ = created_user
        response = api_methods.login_user(payload['email'], payload['password'])
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка логина пользователя с неверным email')
    def test_login_user_with_invalid_email(self, created_user):
        payload, _ = created_user
        wrong_email = payload['email'] + 'wrong'
        response = api_methods.login_user(wrong_email, payload['password'])
        response_data = response.json()
        assert response.status_code == 401
        assert response_data.get('message') == data.MESSAGE_LOGIN_INCORRECT

    @allure.title('Проверка логина пользователя с неверным password')
    def test_login_user_with_invalid_password(self, created_user):
        payload, _ = created_user
        wrong_password = payload['password'] + 'wrong'
        response = api_methods.login_user(payload['email'], wrong_password)
        response_data = response.json()
        assert response.status_code == 401
        assert response_data.get('message') == data.MESSAGE_LOGIN_INCORRECT