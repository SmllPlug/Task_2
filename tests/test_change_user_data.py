import allure


from utils import helpers


class TestChangeUserData:
    @allure.title('Проверка смены email у авторизованного пользователя, статус код 200')
    @allure.step('Отправка PATCH запроса для смены email у авторизованного пользователя')
    def test_change_email_authorized_user_status_code(self, created_user):
        payload, access_token = created_user
        new_payload = {
                'email': payload['email'] + 'new',
                'name': payload['name'],
                'password': payload['password']
        }
        response = helpers.change_user_data(new_payload, access_token)
        assert response.status_code == 200

    @allure.title('Проверка смены email у авторизованного пользователя, в ответе возвращается success: true')
    @allure.step('Отправка PATCH запроса для смены email у авторизованного пользователя')
    def test_change_email_authorized_user_message(self, created_user):
        payload, access_token = created_user
        new_payload = {
                'email': payload['email'] + 'new',
                'name': payload['name'],
                'password': payload['password']
        }
        response = helpers.change_user_data(new_payload, access_token)
        assert response.json().get('success') is True

    @allure.title('Проверка смены email на уже существующую у авторизованного пользователя, статус код 403')
    @allure.step('Отправка PATCH запроса для смены email у авторизованного пользователя')
    def test_change_email_to_exists_email_authorized_user_status_code(self, cleanup_user):
        first_user = helpers.create_user_data()
        first_response = helpers.create_user(first_user)
        first_access_token = first_response.json().get('accessToken')
        cleanup_user(first_access_token)
        second_user = helpers.create_user_data()
        second_response = helpers.create_user(second_user)
        second_access_token = second_response.json().get('accessToken')
        cleanup_user(second_access_token)
        new_payload = {
            'email': first_user['email'],
            'name': second_user['name'],
            'password': second_user['password']
        }
        response = helpers.change_user_data(new_payload, second_access_token)
        assert response.status_code == 403

    @allure.title('Проверка смены email на уже существующую у авторизованного пользователя, в ответе возвращается сообщение "User with such email already exists"')
    @allure.step('Отправка PATCH запроса для смены email у авторизованного пользователя')
    def test_change_email_to_exists_email_authorized_user_message(self, cleanup_user):
        first_user = helpers.create_user_data()
        first_response = helpers.create_user(first_user)
        first_access_token = first_response.json().get('accessToken')
        cleanup_user(first_access_token)
        second_user = helpers.create_user_data()
        second_response = helpers.create_user(second_user)
        second_access_token = second_response.json().get('accessToken')
        cleanup_user(second_access_token)
        new_payload = {
            'email': first_user['email'],
            'name': second_user['name'],
            'password': second_user['password']
        }
        response = helpers.change_user_data(new_payload, second_access_token)
        assert response.json().get('message') == 'User with such email already exists'

    @allure.title('Проверка смены пароля у авторизованного пользователя, статус код 200')
    @allure.step('Отправка PATCH запроса для смены пароля у авторизованного пользователя')
    def test_change_password_authorized_status_code(self, created_user):
        payload, access_token = created_user
        new_payload = {
                'email': payload['email'],
                'name': payload['name'],
                'password': payload['password'] + 'new'
        }
        response = helpers.change_user_data(new_payload, access_token)
        assert response.status_code == 200

    @allure.title('Проверка смены пароля у авторизованного пользователя, в ответе возвращается success: true')
    @allure.step('Отправка PATCH запроса для смены пароля у авторизованного пользователя')
    def test_change_password_authorized_user_message(self, created_user):
        payload, access_token = created_user
        new_payload = {
                'email': payload['email'],
                'name': payload['name'],
                'password': payload['password'] + 'new'
        }
        response = helpers.change_user_data(new_payload, access_token)
        assert response.json().get('success') is True

    @allure.title('Проверка смены имени у авторизованного пользователя, статус код 200')
    @allure.step('Отправка PATCH запроса для смены имени у авторизованного пользователя')
    def test_change_name_authorized_user_status_code(self, created_user):
        payload, access_token = created_user
        new_payload = {
                'email': payload['email'],
                'name': payload['name'] + 'new',
                'password': payload['password']
        }
        response = helpers.change_user_data(new_payload, access_token)
        assert response.status_code == 200

    @allure.title('Проверка смены имени у авторизованного пользователя, в ответе возвращается success: true')
    @allure.step('Отправка PATCH запроса для смены имени у авторизованного пользователя')
    def test_change_name_authorized_user_message(self, created_user):
        payload, access_token = created_user
        new_payload = {
                'email': payload['email'],
                'name': payload['name'] + 'new',
                'password': payload['password']
        }
        response = helpers.change_user_data(new_payload, access_token)
        assert response.json().get('success') is True

    @allure.title('Проверка смены email у неавторизованного пользователя, статус код 401')
    @allure.step('Отправка PATCH запроса для смены email у неавторизованного пользователя')
    def test_change_email_unauthorized_user_status_code(self):
        new_payload = {
            'email': 'newemail@test.ru'
        }
        response = helpers.change_user_data(new_payload)
        assert response.status_code == 401


    @allure.title('Проверка смены email у неавторизованного пользователя, в ответе возвращается сообщение "You should be authorised"')
    @allure.step('Отправка PATCH запроса для смены email у неавторизованного пользователя')
    def test_change_email_unauthorized_user_message(self):
        new_payload = {
            'email': 'newemail@test.ru'
        }
        response = helpers.change_user_data(new_payload)
        assert response.json().get('message') == 'You should be authorised'

    @allure.title('Проверка смены пароля у неавторизованного пользователя, статус код 401')
    @allure.step('Отправка PATCH запроса для смены пароля у неавторизованного пользователя')
    def test_change_password_unauthorized_status_code(self):
        new_payload = {
            'password': 'newpassword'
        }
        response = helpers.change_user_data(new_payload)
        assert response.status_code == 401

    @allure.title('Проверка смены пароля у неавторизованного пользователя, в ответе возвращается сообщение "You should be authorised"')
    @allure.step('Отправка PATCH запроса для смены пароля у неавторизованного пользователя')
    def test_change_password_unauthorized_user_message(self):
        new_payload = {
            'password': 'newpassword'
        }
        response = helpers.change_user_data(new_payload)
        assert response.json().get('message') == 'You should be authorised'

    @allure.title('Проверка смены имени у неавторизованного пользователя, статус код 401')
    @allure.step('Отправка PATCH запроса для смены email у неавторизованного пользователя')
    def test_change_name_unauthorized_user_status_code(self):
        new_payload = {
            'name': 'newname'
        }
        response = helpers.change_user_data(new_payload)
        assert response.status_code == 401

    @allure.title('Проверка смены имени у неавторизованного пользователя, в ответе возвращается сообщение "You should be authorised"')
    @allure.step('Отправка PATCH запроса для смены почты у неавторизованного пользователя')
    def test_change_name_unauthorized_user_message(self):
        new_payload = {
            'name': 'newname'
        }
        response = helpers.change_user_data(new_payload)
        assert response.json().get('message') == 'You should be authorised'