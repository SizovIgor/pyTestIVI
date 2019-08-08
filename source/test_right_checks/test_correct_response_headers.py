# -*- coding: utf-8 -*-

"""
Проверка правильности заголовков ответов

setup_module: Предварительная настройка на уровне модуля.
teardown_module: Действия по завершению всех тестов.
"""

import pytest
from source.option import *


@pytest.yield_fixture(scope='module', autouse=True)
def setup_and_teardown(create_session):
    global session
    session = create_session
    yield
    session.close()


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
