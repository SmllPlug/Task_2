import allure


from utils import api_methods
from utils import data


class TestCreateOrder:
    @allure.title('Проверка создания заказа авторизованным пользователем')
    def test_create_order_with_authorized_user(self, created_user):
        _, access_token = created_user
        response = api_methods.create_order(data.INGREDIENTS, access_token)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка создания заказа неавторизованным пользователем')
    def test_create_order_with_unauthorized_user(self):
        response = api_methods.create_order(data.INGREDIENTS)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data.get('success') is True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, created_user):
        _, access_token = created_user
        response = api_methods.create_order(data.EMPTY_INGREDIENTS, access_token)
        response_data = response.json()
        assert response.status_code == 400
        assert response_data.get('message') == data.MESSAGE_INGREDIENTS_REQUIRED

    @allure.title('Проверка создания заказа с неверным хэшем ингредиентов')
    def test_create_order_with_invalid_ingredients_hash(self, created_user):
        _, access_token = created_user
        response = api_methods.create_order(data.INVALID_INGREDIENTS, access_token)
        assert response.status_code == 500
        assert data.MESSAGE_INTERNAL_SERVER_ERROR in response.text