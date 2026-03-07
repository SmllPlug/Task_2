import allure


from utils import helpers
from utils import data


class TestCreateOrder:
    @allure.title('Проверка создания заказа авторизованным пользователем, статус код 200')
    @allure.step('Отправка POST запроса для создания заказа авторизованным пользователем')
    def test_create_order_with_authorized_user_status_code(self, created_user):
        _, access_token = created_user
        response = helpers.create_order(data.INGREDIENTS, access_token)
        assert response.status_code == 200


    @allure.title('Проверка создания заказа авторизованным пользователем, в ответе возвращается success: true')
    @allure.step('Отправка POST запроса для создания заказа авторизованным пользователем')
    def test_create_order_with_authorized_user_message(self, created_user):
        _, access_token = created_user
        response = helpers.create_order(data.INGREDIENTS, access_token)
        assert response.json().get('success') is True

    @allure.title('Проверка создания заказа неавторизованным пользователем, статус код 200')
    @allure.step('Отправка POST запроса для создания заказа неавторизованным пользователем')
    def test_create_order_with_unauthorized_user_status_code(self):
        response = helpers.create_order(data.INGREDIENTS)
        assert response.status_code == 200


    @allure.title('Проверка создания заказа неавторизованным пользователем, в ответе возвращается success: true')
    @allure.step('Отправка POST запроса для создания заказа неавторизованным пользователем')
    def test_create_order_with_unauthorized_user_message(self):
        response = helpers.create_order(data.INGREDIENTS)
        assert response.json().get('success') is True

    @allure.title('Проверка создания заказа без ингредиентов, статус код 400')
    @allure.step('Отправка POST запроса для создания без ингредиентов')
    def test_create_order_without_ingredients_status_code(self, created_user):
        _, access_token = created_user
        response = helpers.create_order(data.EMPTY_INGREDIENTS, access_token)
        assert response.status_code == 400

    @allure.title('Проверка создания заказа без ингредиентов, в ответе возвращается сообщение "Ingredient ids must be provided"')
    @allure.step('Отправка POST запроса для создания без ингредиентов')
    def test_create_order_without_ingredients_message(self, created_user):
        _, access_token = created_user
        response = helpers.create_order(data.EMPTY_INGREDIENTS, access_token)
        assert response.json().get('message') == 'Ingredient ids must be provided'

    @allure.title('Проверка создания заказа с неверным хэшом ингредиентов, статус код 500')
    @allure.step('Отправка POST запроса для создания заказа с неверным хэшом ингредиентов')
    def test_create_order_with_invalid_ingredients_hash_status_code(self,created_user):
        _, access_token = created_user
        response = helpers.create_order(data.INVALID_INGREDIENT, access_token)
        assert response.status_code == 500

    @allure.title('Проверка создания заказа с неверным хэшом ингредиентов, в ответе возвращается текст "Internal server message"')
    @allure.step('Отправка POST запроса для создания заказа с неверным хэшом ингредиентов')
    def test_create_order_with_invalid_ingredients_hash_message(self,created_user):
        _, access_token = created_user
        response = helpers.create_order(data.INVALID_INGREDIENT, access_token)
        assert 'Internal Server Error' in response.text