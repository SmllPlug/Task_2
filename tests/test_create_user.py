import allure


from utils import helpers


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя, статус код 200')
    @allure.step('Отправка POST запроса для создания пользователя')
    def test_create_user_with_valid_data_status_code(self, cleanup_user):
        user_data = helpers.create_user_data()
        response = helpers.create_user(user_data)
        access_token = response.json().get('accessToken')
        cleanup_user(access_token)
        assert response.status_code == 200

    @allure.title('Проверка создания уникального пользователя, в ответе возвращается success: true')
    @allure.step('Отправка POST запроса для создания пользователя')
    def test_create_user_with_valid_data_message(self, cleanup_user):
        user_data = helpers.create_user_data()
        response = helpers.create_user(user_data)
        access_token = response.json().get('accessToken')
        cleanup_user(access_token)
        assert response.json().get('success') is True

    @allure.title('Проверка создания пользователя, который уже зарегестирован, статус код 403')
    @allure.step('Отправка POST запроса для создания пользователя, который уже зарегистрирован')
    def test_create_user_with_existing_user_status_code(self, created_user):
        payload, _ = created_user
        response = helpers.create_user(payload)
        assert response.status_code == 403

    @allure.title('Проверка создания пользователя, который уже зарегестирован, в ответе возвращается сообщение "User already exists"')
    @allure.step('Отправка POST запроса для создания пользователя, который уже зарегистрирован')
    def test_create_user_with_existing_user_message(self, created_user):
        payload, _ = created_user
        response = helpers.create_user(payload)
        assert response.json().get('message') == 'User already exists'

    @allure.title('Проверка создания пользователя без обязательного поля email, статус код 403')
    @allure.step('Отправка POST запроса для создания пользователя без email')
    def test_create_user_without_email_status_code(self):
        payload = helpers.create_user_data_without_email()
        response = helpers.create_user(payload)
        assert response.status_code == 403

    @allure.title('Проверка создания пользователя без обязательного поля email, в ответе возвращается сообщение "Email, password and name are required fields"')
    @allure.step('Отправка POST запроса для создания пользователя без email')
    def test_create_user_without_email_message(self):
        payload = helpers.create_user_data_without_email()
        response = helpers.create_user(payload)
        assert response.json().get('message') == 'Email, password and name are required fields'

    @allure.title('Проверка создания пользователя без обязательного поля password, статус код 403')
    @allure.step('Отправка POST запроса для создания пользователя без password')
    def test_create_user_without_password_status_code(self):
        payload = helpers.create_user_data_without_password()
        response = helpers.create_user(payload)
        assert response.status_code == 403

    @allure.title('Проверка создания пользователя без обязательного поля password, в ответе возвращается сообщение "Email, password and name are required fields"')
    @allure.step('Отправка POST запроса для создания пользователя без password')
    def test_create_user_without_password_message(self):
        payload = helpers.create_user_data_without_password()
        response = helpers.create_user(payload)
        assert response.json().get('message') == 'Email, password and name are required fields'


    @allure.title('Проверка создания пользователя без обязательного поля name, статус код 403')
    @allure.step('Отправка POST запроса для создания пользователя без name')
    def test_create_user_without_name_status_code(self):
        payload = helpers.create_user_data_without_name()
        response = helpers.create_user(payload)
        assert response.status_code == 403

    @allure.title('Проверка создания пользователя без обязательного поля name, в ответе возвращается сообщение "Email, password and name are required fields"')
    @allure.step('Отправка POST запроса для создания пользователя без name')
    def test_create_user_without_name_message(self):
        payload = helpers.create_user_data_without_name()
        response = helpers.create_user(payload)
        assert response.json().get('message') == 'Email, password and name are required fields'