import requests
import random
import string


from utils.urls import Urls
from allure import step


@step('Генерация рандомной строки длинной {length}')
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string
@step('Генерация рандомной строки длинной {length}')
def generate_invalid_hash(length=24):
        chars = string.ascii_lowercase + string.digits
        random_string = ''.join(random.choice(chars) for _ in range(length))
        return random_string

@step('Создание данных для регистрации пользователя')
def create_user_data():
        email = f'{generate_random_string(10)}@test.com'
        password = generate_random_string(10)
        name = generate_random_string(10)
        return {
                'email': email,
                'password': password,
                'name': name
        }

@step('Создание данных для регистрации пользователя без email')
def create_user_data_without_email():
        password = generate_random_string(10)
        name = generate_random_string(10)
        return {
                'password': password,
                'name': name
        }

@step('Создание данных для регистрации пользователя без password')
def create_user_data_without_password():
        email = f'{generate_random_string(10)}@test.com'
        name = generate_random_string(10)
        return {
                'email': email,
                'name': name
        }

@step('Создание данных для регистрации пользователя без name')
def create_user_data_without_name():    
        email = f'{generate_random_string(10)}@test.com'
        password = generate_random_string(10)
        return {
                'email': email,
                'password': password
        }

@step('Создание пользователя')
def create_user(payload):
        return requests.post(Urls.CREATE_USER_URL, json=payload)

@step('Авторизация пользователя')
def login_user(email, password):
        payload = {
                'email': email,
                'password': password
        }
        response = requests.post(Urls.LOGIN_URL, json=payload)
        return response

@step('Удаление пользователя')
def delete_user(access_token):
    headers = {
        'Authorization': access_token
    }
    return requests.delete(Urls.CHANGE_USER_DATA_URL, headers=headers)

@step('Изменение данных пользователя')
def change_user_data(payload, access_token=None):
    headers = {}
    if access_token:
        headers['Authorization'] = access_token
    return requests.patch(Urls.CHANGE_USER_DATA_URL, json=payload, headers=headers)

@step('Создание заказа')
def create_order(ingredients, access_token=None):
    payload = {
        'ingredients': ingredients
    }
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