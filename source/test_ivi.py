# -*- coding: utf-8 -*-

"""
Базовая проверка конективити

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
session = None


@pytest.yield_fixture(scope='module', autouse=True)
def setup_and_teardown(create_session):
    global session
    session = create_session
    yield
    session.close()


# @pytest.mark.skip
def test_get_characters():
    """
    Проверка доступности метода GET /characters

    :return:  Fail/Pass
    """
    # global session
    # session = setup
    response = session.get(base_url.format(characters))
    assert response.ok


# @pytest.mark.skip
def test_get_character_by_name(name: str = 'Ajak'):
    """
    Проверка доступности метода GET /character/{name}

    :param name: Имя персонажа, по которому запрашивается информация
    :return: Fail/Pass
    """
    response = session.get(base_url.format(character_by_name.format(name)))
    assert response.ok


# @pytest.mark.skip
def test_post_character(post_setup):
    """
    Проверка доступности метода POST /character

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
    assert response.ok


# @pytest.mark.skip
def test_put_character_by_name(post_setup, name: str = 'Ajak'):
    """
    Проверка доступности метода PUT /character/{name}

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
    assert response.ok


# @pytest.mark.skip
def test_delete_character_by_name(name: str = 'Ajak'):
    """
    Проверка доступности метода Delete /character/{name}

    :param name: имя персонажа для удаления
    :return: Fail/Pass
    """
    response = session.delete(base_url.format(character_by_name.format(name)))
    assert response.ok


# @pytest.mark.skip
def test_post_reset():
    """
    Проверка доступности метода POST /reset

    :return: Fail/Pass
    """
    response = session.post(base_url.format(reset))
    assert response.ok
