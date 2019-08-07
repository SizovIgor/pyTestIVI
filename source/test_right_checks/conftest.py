"""
Тут должны быть настройки для тестов соответствующей категории
"""
import pytest
import random
import string


@pytest.fixture(scope='module', params=["1", "2"])
def delete_auth(request):
    cyrilic_symbols = range(ord('А'), ord('я'))
    rand_symbols = ''.join(chr(random.randint(cyrilic_symbols)) for i in range(10))
    yield
    print('Auth was restored')


@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass
