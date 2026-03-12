from utils import helpers


INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f"
]

INVALID_INGREDIENTS = [helpers.generate_invalid_hash(),
                      helpers.generate_invalid_hash()]

EMPTY_INGREDIENTS = []

MESSAGE_USER_ALREADY_EXISTS = 'User already exists'
MESSAGE_REQUIRED_FIELDS = 'Email, password and name are required fields'
MESSAGE_LOGIN_INCORRECT = 'email or password are incorrect'
MESSAGE_USER_EMAIL_EXISTS = 'User with such email already exists'
MESSAGE_UNAUTHORIZED = 'You should be authorised'
MESSAGE_INGREDIENTS_REQUIRED = 'Ingredient ids must be provided'
MESSAGE_INTERNAL_SERVER_ERROR = 'Internal Server Error'