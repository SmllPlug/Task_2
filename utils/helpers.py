import random
import string


from allure import step


@step('Генерация случайной строки длиной {length}')
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@step('Генерация невалидного хэша')
def generate_invalid_hash(length=24):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@step('Создание данных пользователя')
def create_user_data():
    return {
        'email': f'{generate_random_string(10)}@test.com',
        'password': generate_random_string(10),
        'name': generate_random_string(10)
    }

@step('Создание данных пользователя без email')
def create_user_data_without_email():
    return {
        'password': generate_random_string(10),
        'name': generate_random_string(10)
    }

@step('Создание данных пользователя без password')
def create_user_data_without_password():
    return {
        'email': f'{generate_random_string(10)}@test.com',
        'name': generate_random_string(10)
    }

@step('Создание данных пользователя без name')
def create_user_data_without_name():
    return {
        'email': f'{generate_random_string(10)}@test.com',
        'password': generate_random_string(10)
    }