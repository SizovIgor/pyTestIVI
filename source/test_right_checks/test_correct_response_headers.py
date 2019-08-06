# -*- coding: utf-8 -*-

"""
Проверка правильности заголовков ответов

setup_module: Предварительная настройка на уровне модуля.
teardown_module: Действия по завершению всех тестов.
"""

import pytest
import requests

base_url = 'http://rest.test.ivi.ru{}'
characters = '/characters'
character = '/character'
characters_by_name = '/characters/{}'
character_by_name = '/character/{}'
reset = "/reset"

session = requests.Session()
proxies = {}


def setup_module(module) -> None:
    """
    Обязательно необходимо указать правильные значения username:password

    :return: None
    """
    print("MODULE SETUP")
    session.proxies = proxies
    session.auth = ('username', 'password')


def teardown_module(module) -> None:
    """
    В данном случае закрытие сессии.

    :return: None
    """
    session.close()
    print("MODULE TEARDOWN")


@pytest.fixture()
def post_setup(request) -> None:
    """
    Фикстура по обновлению заголовков для методов, на уровне теста, где необходимо отправлять json на сервер.

    :return: None
    """
    session.headers['Content-type'] = 'Application/json'

    def post_teardown():
        """
        Метод вызываемый для восстановления заголовков сессии, после выполнения теста.

        :return: None
        """
        session.headers.pop('Content-type')

    request.addfinalizer(post_teardown)


# @pytest.mark.skip
def test_get_characters():
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос GET /characters

    :return: Fail/Pass
    """
    response = session.get(base_url.format(characters))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
def test_get_character_by_name(name: str = 'Ajak'):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос GET /character/{name}

    :param name: имя персонажа для запроса по нему информации
    :return: Fail/Pass
    """
    response = session.get(base_url.format(character_by_name.format(name)))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
def test_post_character(post_setup):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос POST /character

    :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
    :return: Fail/Pass
    """
    data = {
        "name": "xxx_777",
        "universe": "xxx_7771",
        "education": "xxx_7772",
        "weight": 777,
        "height": 7.71,
        "identity": "xxx_7773",
        "other_aliases": "None"
    }

    response = session.post(
        url=base_url.format(character),
        json=data
    )
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
def test_put_character_by_name(post_setup, name: str = 'Ajak'):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос PUT /character/{name}

    :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
    :param name: имя персонажа для обновления по нему информации
    :return: Fail/Pass
    """
    data = {
        'education': 'Unrevealed',
        'height': 99,
        'identity': 'Secret',
        'name': 'Ajak',
        'other_aliases': 'Tecumotzin, Lord of Flight',
        'universe': 'Marvel Universe',
        'weight': 999.0
    }
    response = session.put(
        url=base_url.format(character_by_name.format(name)),
        json=data
    )
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
def test_delete_character_by_name(name: str = 'Ajak'):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос DELETE /character/{name}

    :param name: имя персонажа для удаления по нему информации
    :return: Fail/Pass
    """
    response = session.delete(base_url.format(character_by_name.format(name)))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
# @pytest.mark.xfail()
def test_post_reset():
    """
    Тест-кейс направленный на проверку корректности заголовка от сервера в ответ на запрос POST /reset

    :return: Fail/Pass
    """
    response = session.post(base_url.format(reset))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
