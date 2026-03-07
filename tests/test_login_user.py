import allure


from utils import helpers


class TestLoginUser:
    @allure.title('Проверка логина пользователя, статус код 200')
    @allure.step('Отправка POST запроса для логина пользователя')
    def test_login_user_with_existing_user_status_code(self, created_user):
        payload, _ = created_user
        response = helpers.login_user(payload['email'], payload['password'])
        assert response.status_code == 200

    @allure.title('Проверка логина пользователя, в ответе возвращается success: true')
    @allure.step('Отправка POST запроса для логина пользователя')
    def test_login_user_with_existing_user_message(self, created_user):
        payload, _ = created_user
        response = helpers.login_user(payload['email'], payload['password'])
        assert response.json().get('success') is True

    @allure.title('Проверка логина пользователя с неправильным email, статус код 401')
    @allure.step('Отправка POST запроса для логина пользователя с неправильным email')
    def test_login_user_with_invalid_email_status_code(self, created_user):
        payload, _ = created_user
        wrong_email = payload['email'] + 'wrong'
        response = helpers.login_user(wrong_email, payload['password'])
        assert response.status_code == 401

    @allure.title('Проверка логина пользователя с неправильным email, в ответе возвращается сообщение "email or password are incorrect"')
    @allure.step('Отправка POST запроса для логина пользователя с неправильным email')
    def test_login_user_with_invalid_email_message(self, created_user): 
        payload, _ = created_user
        wrong_email = payload['email'] + 'wrong'
        response = helpers.login_user(wrong_email, payload['password'])
        assert response.json().get('message') == 'email or password are incorrect'

    @allure.title('Проверка логина пользователя с неправильным password, статус код 401')
    @allure.step('Отправка POST запроса для логина пользователя с неправильным password')
    def test_login_user_with_invalid_password_status_code(self, created_user):
        payload, _ = created_user
        wrong_password = payload['password'] + 'wrong'
        response = helpers.login_user(payload['email'], wrong_password)
        assert response.status_code == 401

    @allure.title('Проверка логина пользователя с неправильным password, в ответе возвращается сообщение "email or password are incorrect"')
    @allure.step('Отправка POST запроса для логина пользователя с неправильным password')
    def test_login_user_with_invalid_password_message(self, created_user):
        payload, _ = created_user
        wrong_password = payload['password'] + 'wrong'
        response = helpers.login_user(payload['email'], wrong_password)
        assert response.json().get('message') == 'email or password are incorrect'