import allure


from utils import api_methods
from utils import data


class TestGetOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_orders_with_authorized_user(self, created_user):
        _, access_token = created_user
        api_methods.create_order(data.INGREDIENTS, access_token)
        response = api_methods.get_orders(access_token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка получения заказов неавторизованного пользователя')
    def test_get_orders_with_unauthorized_user(self):
        response = api_methods.get_orders()
        response_data = response.json()
        assert response.status_code == 401
        assert response_data.get('message') == data.MESSAGE_UNAUTHORIZED