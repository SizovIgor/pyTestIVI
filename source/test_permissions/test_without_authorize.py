# -*- coding: utf-8 -*-

"""
Проверки коректности ответа от сервера на запросы различные запросы от неавторизованного пользователя
"""

import pytest
from source.option import *


@pytest.yield_fixture(scope='module', autouse=True)
def setup_and_teardown(create_session, delete_auth):
    """
    Фикстура создающая настройки окружения для начала работы тестов.

    :param create_session: вызов фикстуры для создания объекта сессии
    :param delete_auth: вызов фикстуры для удаления авторизации из объекта сессии
    :return: None
    """
    global session
    session = create_session
    yield
    session.close()


# @pytest.mark.skip
def test_get_characters_not_authorized():
    """
    Тест-кейс направленный на проверку корректности ответа от сервера на запрос GET /characters от
    не авторизованного пользователя

    :return: Fail/Pass
    """
    response = session.get(base_url.format(characters))
    assert response.status_code == 401


# @pytest.mark.skip
def test_get_character_by_name_not_authorized(name: str = 'Ajak'):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос GET /character/{name} от
    не авторизованного пользователя

    :param name: имя персонажа для запроса по нему информации
    :return: Fail/Pass
    """
    response = session.get(base_url.format(character_by_name.format(name)))
    assert response.status_code == 401


# @pytest.mark.skip
def test_post_character_not_authorized(post_setup):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос POST /character от
    не авторизованного пользователя

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
    assert response.status_code == 401


# @pytest.mark.skip
def test_put_character_by_name_not_authorized(post_setup, name: str = 'Ajak'):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос PUT /character/{name} от
    не авторизованного пользователя

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
    assert response.status_code == 401


# @pytest.mark.skip
def test_delete_character_by_name_not_authorized(name: str = 'Ajak'):
    """
    Тест-кейс направленный на проверку корректности заголовка ответа от сервера на запрос DELETE /character/{name} от
    не авторизованного пользователя

    :param name: имя персонажа для удаления по нему информации
    :return: Fail/Pass
    """
    response = session.delete(base_url.format(character_by_name.format(name)))
    assert response.status_code == 401


def test_post_reset_not_authorized():
    """
    Тест-кейс направленный на проверку корректности заголовка от сервера в ответ на запрос POST /reset от
    не авторизованного пользователя

    :return: Fail/Pass
    """
    response = session.post(base_url.format(reset))
    assert response.status_code == 401
