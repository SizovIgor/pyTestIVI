# -*- coding: utf-8 -*-

"""
Проверка правильности заголовков ответов
"""

import pytest
import requests
import json

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
proxies = {
    "http": "http://isizov:aa11aa11@proxy.tsc.ts:8080",
    "https": "https://isizov:aa11aa11@proxy.tsc.ts:8080",
}


def setup_module(module):
    print("module setup")
    session.proxies = proxies
    session.auth = ('ya.shok.ya@yandex.ru', 'hgJH768Cv23')


def teardown_module(module):
    session.close()
    print("module teardown")


@pytest.fixture()
def post_setup(request):
    session.headers['Content-type'] = 'Application/json'

    def post_teardown():
        session.headers.pop('Content-type')

    request.addfinalizer(post_teardown)


print('START')


# @pytest.mark.xfail(
#     condition=session.get(base_url.format(characters)).status_code != 200,
#     reason='The remote server is unavailable'
# )
class TestGetCharactersWithValidCases:

    def test_first_query(self):
        print('test_first_query')
        response = session.get(base_url.format(characters))
        assert len(response.json()['result']) >= 0

    def test_check_changed_data(self, post_setup):
        response_source_data = session.get(base_url.format(characters))
        source_data_json = response_source_data.json()
        name = None

        if 'result' in source_data_json:
            if len(source_data_json['result']) > 0:
                name = source_data_json['result'][0]['name']
            else:
                pytest.skip(r'Response don\'t have characters')
        else:
            pytest.fail(r'Test failed because response don\'t have result field')
            print('Response contain:', source_data_json)

        one_character = source_data_json['result'][0]
        one_character['education'] = 'something_universal-3345'
        response_change_data = session.put(
            url=base_url.format(character_by_name.format(name)),
            json=one_character,
        )
        print(response_change_data.request,
              response_change_data.text,
              response_change_data.ok, )

        if not response_change_data.ok:
            print(response_change_data.text)
            pytest.fail('Response is not OK')
        response_changed_data = session.get(base_url.format(characters))

        changed_data_json = response_changed_data.json()['result']
        education = [k['education'] for k in filter(lambda x: x['name'] == name, changed_data_json)]
        if len(education) > 1:
            print(f'Attetion! The characters with name "{name}" is duplicated {len(education)} times!')
            # pytest.xfail(f'Attetion! The characters with name {name} is duplicated {len(education)} times!')
        elif len(education) < 1:
            print(f'Attetion! The characters with name "{name}" was lost')
            # pytest.xfail(f'Attetion! The characters with name {name} is duplicated {len(education)} times!')

        for name_of_edu in education:
            print(name_of_edu, name_of_edu == one_character['education'])

    def test_check_deleted_data(self):
        response_source_data = session.get(base_url.format(characters))
        source_data_json = response_source_data.json()
        name = None

        if 'result' in source_data_json:
            if len(source_data_json['result']) > 0:
                name = source_data_json['result'][0]['name']
            else:
                pytest.skip(r'Response don\'t have characters')
        else:
            pytest.fail(r'Test failed because response don\'t have result field')
            print('Response contain:', source_data_json)

        response_deleted_data = session.delete(
            url=base_url.format(character_by_name.format(name)),
        )

        if not response_deleted_data.ok:
            print(response_deleted_data.text)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        changed_data_json = response_changed_data.json()['result']
        list_names = [k['name'] for k in changed_data_json]
        assert name not in list_names
        # if len(characters_list_by_name) > 0:
        # print(f'Attetion! The characters with name {name} is duplicated {len(education)} times!')
        # pytest.fail(f'Attetion! The characters with name {name} was not delete')

    def test_check_added_data(self, post_setup):
        response_source_data = session.get(base_url.format(characters))
        source_data_json = response_source_data.json()['result']
        name = 'xxx_777_123_321'
        is_name_exists = bool(list(filter(lambda x: x['name'] == name, source_data_json)))
        if not is_name_exists:
            name *= 2
        data = {
            "name": name,
            "universe": "xxx_7771",
            "education": "xxx_7772",
            "weight": 777,
            "height": 7.71,
            "identity": "xxx_7773",
            "other_aliases": "None"
        }

        response_added_data = session.post(
            url=base_url.format(character),
            json=data,
        )

        if not response_added_data.ok:
            print(response_added_data.text)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        changed_data_json = response_changed_data.json()['result']
        new_names = [k['name'] for k in changed_data_json]
        assert name in new_names

    # @pytest.mark.xfail
    def test_check_deleted_all_data(self, post_setup):
        response_source_data = session.get(base_url.format(characters))
        source_data_json = response_source_data.json()['result']
        if len(source_data_json) == 0:
            name = 'xxx_777_123_321'
            data = {
                "name": name,
                "universe": "xxx_7771",
                "education": "xxx_7772",
                "weight": 777,
                "height": 7.71,
                "identity": "xxx_7773",
                "other_aliases": "None"
            }

            session.post(
                url=base_url.format(character),
                json=data,
            )

        response_reset_data = session.post(base_url.format(reset))
        if not response_reset_data.ok:
            print(response_reset_data.text)
            pytest.fail('Response is not OK')
        print(response_reset_data.request,
              response_reset_data.text,
              response_reset_data.ok, )

        response_changed_data = session.get(base_url.format(characters))
        assert len(response_changed_data.json()['result']) == 0

# class TestSecondClass:
#     # @pytest.mark.skip
#     def test_get_character_by_name(name: str = 'Ajak'):
#         response = session.get(base_url.format(character_by_name.format(name)))
#         assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
#
# # @pytest.mark.skip
# def test_post_character(self, post_setup):
#     data = {
#         "name": "xxx_777",
#         "universe": "xxx_7771",
#         "education": "xxx_7772",
#         "weight": 777,
#         "height": 7.71,
#         "identity": "xxx_7773",
#         "other_aliases": "None"
#     }
#
#     response = session.post(
#         url=base_url.format(character),
#         json=data
#     )
#     assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
#
# # @pytest.mark.skip
# def test_put_character_by_name(self, post_setup, name: str = 'Ajak'):
#     data = {
#         'education': 'Unrevealed',
#         'height': 99,
#         'identity': 'Secret',
#         'name': 'Ajak',
#         'other_aliases': 'Tecumotzin, Lord of Flight',
#         'universe': 'Marvel Universe',
#         'weight': 999.0
#     }
#     response = session.put(
#         url=base_url.format(character_by_name.format(name)),
#         json=data
#     )
#     assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
#
# # @pytest.mark.skip
# def test_delete_character_by_name(self, name: str = 'Ajak'):
#     response = session.delete(base_url.format(character_by_name.format(name)))
#     assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
#
# # @pytest.mark.skip
# def test_post_reset(self, ):
#     response = session.post(base_url.format(reset))
#     assert str(response.headers['Content-type']).lower() == 'Application/json'.lower()
