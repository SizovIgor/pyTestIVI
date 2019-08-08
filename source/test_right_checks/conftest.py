"""
Файл фикстур, содержит в себе фикстуры для данной категории тестов.
"""
import pytest
import random
import string

cyrilic_uppercase = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrilic_lowercase = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
cyrilic_letters = cyrilic_lowercase + cyrilic_uppercase


@pytest.fixture(
    params=[cyrilic_letters, string.ascii_letters, string.punctuation],
    ids=['cyrilic_letters', 'latin_letters', 'punctuation_symbols']
)
def random_different_language_symbols(request):
    string_length = 10
    random_characters = request.param + string.digits + string.whitespace
    return ''.join(random.choice(random_characters) for i in range(string_length))
