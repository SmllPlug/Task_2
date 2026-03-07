import allure


from utils import helpers


class TestGetOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя, статус код 200')
    @allure.step('Отправка GET запроса для получения заказов авторизованного пользователя')
    def test_get_orders_with_authorized_user_status_code(self, created_user):
        _, access_token = created_user
        response = helpers.get_orders(access_token)
        assert response.status_code == 200
    
    @allure.title('Проверка получения заказов авторизованного пользователя, в ответе возвращается success: true')
    @allure.step('Отправка GET запроса для получения заказов авторизованного пользователя')
    def test_get_orders_with_authorized_user_message(self, created_user):
        _, access_token = created_user
        response = helpers.get_orders(access_token)
        assert response.json().get('success') is True

    @allure.title('Проверка получения заказов неавторизованного пользователя, статус код 401')
    @allure.step('Отправка GET запроса для получения заказов неавторизованного пользователя')
    def test_get_orders_with_unauthorized_user_status_code(self):
        response = helpers.get_orders()
        assert response.status_code == 401

    @allure.title('Проверка получения заказов неавторизованного пользователя, в ответе возвращается сообщение "You should be authorised"')
    @allure.step('Отправка GET запроса для получения заказов неавторизованного пользователя')
    def test_get_orders_with_unauthorized_user_message(self):
        response = helpers.get_orders()
        assert response.json().get('message') == 'You should be authorised'