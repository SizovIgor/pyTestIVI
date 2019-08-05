# -*- coding: utf-8 -*-

"""
Проверка правильности заголовков ответов
"""

import pytest
import requests

base_url = 'http://rest.test.ivi.ru{}'
characters = '/characters'
character = '/character'
characters_by_name = '/characters/{}'
character_by_name = '/character/{}'
reset = "/reset"

# GET /characters
# GET /character/{name}
#
# POST /character
# PUT /character/{name}
# DELETE /character/{name}
#
# POST /reset

session = requests.Session()
proxies = {}


def setup_module(module):
    print("module setup")
    session.proxies = proxies
    session.auth = ('user', 'hgJH768Cv23')


def teardown_module(module):
    session.close()
    print("module teardown")


@pytest.fixture()
def post_setup(request):
    session.headers['Content-type'] = 'Application/json'

    def post_teardown():
        session.headers.pop('Content-type')

    request.addfinalizer(post_teardown)


# @pytest.mark.skip
def test_get_characters():
    response = session.get(base_url.format(characters))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
def test_get_character_by_name(name: str = 'Ajak'):
    response = session.get(base_url.format(character_by_name.format(name)))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
def test_post_character(post_setup):
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
    response = session.delete(base_url.format(character_by_name.format(name)))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()


# @pytest.mark.skip
# @pytest.mark.xfail()
def test_post_reset():
    response = session.post(base_url.format(reset))
    assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
