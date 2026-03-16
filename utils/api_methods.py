import requests


from allure import step


from utils.urls import Urls


@step('Создание пользователя')
def create_user(payload):
    return requests.post(Urls.CREATE_USER_URL, json=payload)

@step('Авторизация пользователя')
def login_user(email, password):
    payload = {
        'email': email,
        'password': password
    }
    return requests.post(Urls.LOGIN_URL, json=payload)

@step('Удаление пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    return requests.delete(Urls.CHANGE_USER_DATA_URL, headers=headers)

@step('Изменение данных пользователя')
def change_user_data(payload, access_token=None):
    headers = {}
    if access_token:
        headers['Authorization'] = access_token
    return requests.patch(Urls.CHANGE_USER_DATA_URL, json=payload, headers=headers)

@step('Создание заказа')
def create_order(ingredients, access_token=None):
    payload = {'ingredients': ingredients}
    headers = {}
    if access_token:
        headers['Authorization'] = access_token
    return requests.post(Urls.CREATE_ORDER_URL, json=payload, headers=headers)

@step('Получение заказов')
def get_orders(access_token=None):
    headers = {}
    if access_token:
        headers['Authorization'] = access_token
    return requests.get(Urls.GET_ORDER_URL, headers=headers)