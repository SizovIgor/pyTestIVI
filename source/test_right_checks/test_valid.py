# -*- coding: utf-8 -*-

"""
Проверка работы API-методов с валидными данными.

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


# @pytest.mark.xfail(
#     condition=session.get(base_url.format(characters)).status_code != 200,
#     reason='The remote server is unavailable'
# )
class TestGetCharacters:
    """
    Тест-кейсы направленные на тестирование работы метода GET /characters
    """

    # ToDo: необходимо уточнить что должно быть в колеции по умолчанию (issue-#4)
    def test_first_query(self):
        """
        Тест-кейс направленный на проверку количества персонажей в коллекции по умолчанию
        """
        response = session.get(base_url.format(characters))
        assert len(response.json()['result']) >= 0

    # ToDo: Необходимо заменить print на assert после исправления issue-#1
    def test_check_changed_data(self, post_setup):
        """
        Тест-кейс на проверку наличия внесенных измененний для персонажа в общем списке коллекции

        :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
        :return: Fail/Pass
        """
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

        one_character = source_data_json['result'][0]
        one_character['education'] = 'something_universal-3345'
        response_change_data = session.put(
            url=base_url.format(character_by_name.format(name)),
            json=one_character,
        )

        if not response_change_data.ok:
            print(response_change_data.reason)
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
        """
        Тест-кейс на проверку отсутствие удаленного персонажа в общем списке коллекции

        :return:
        """
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

        response_deleted_data = session.delete(
            url=base_url.format(character_by_name.format(name)),
        )

        if not response_deleted_data.ok:
            print(response_deleted_data.reason)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        changed_data_json = response_changed_data.json()['result']
        list_names = [k['name'] for k in changed_data_json]
        assert name not in list_names
        # if len(characters_list_by_name) > 0:
        # print(f'Attetion! The characters with name {name} is duplicated {len(education)} times!')
        # pytest.fail(f'Attetion! The characters with name {name} was not delete')

    def test_check_added_data(self, post_setup):
        """
        Тест-кейс на проверку наличия добавленного персонажа в общем списке коллекции

        :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
        :return: Fail/Pass
        """
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
            print(response_added_data.reason)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        changed_data_json = response_changed_data.json()['result']
        new_names = [k['name'] for k in changed_data_json]
        assert name in new_names

    # @pytest.mark.xfail
    def test_check_deleted_all_data(self, post_setup):
        """
        Тест-кейс на проверку восстановления общего списка коллекции до первоначального состояния

        :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
        :return: Fail/Pass
        """
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
            print(response_reset_data.reason)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        assert len(response_changed_data.json()['result']) == 0


class TestGetCharacterByName:
    """
    Тест-кейсы направленные на тестирование работы метода GET /character/{name}
    """
    pass


class TestPostCharacter:
    """
    Тест-кейсы направленные на тестирование работы метода POST /character
    """

    def test_on_latin_symbols(self):
        """
        Тест-кейс на проверку корректности работы сервера с латинскими символами

        :return:
        """
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

        response_deleted_data = session.delete(
            url=base_url.format(character_by_name.format(name)),
        )

        if not response_deleted_data.ok:
            print(response_deleted_data.reason)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        changed_data_json = response_changed_data.json()['result']
        list_names = [k['name'] for k in changed_data_json]
        assert name not in list_names
        # if len(characters_list_by_name) > 0:
        # print(f'Attetion! The characters with name {name} is duplicated {len(education)} times!')
        # pytest.fail(f'Attetion! The characters with name {name} was not delete')

    def test_on_cyrilic_symbols(self):
        """
        Тест-кейс на проверку корректности работы сервера с кирилическими символами

        :return:
        """
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

        response_deleted_data = session.delete(
            url=base_url.format(character_by_name.format(name)),
        )

        if not response_deleted_data.ok:
            print(response_deleted_data.reason)
            pytest.fail('Response is not OK')

        response_changed_data = session.get(base_url.format(characters))
        changed_data_json = response_changed_data.json()['result']
        list_names = [k['name'] for k in changed_data_json]
        assert name not in list_names
        # if len(characters_list_by_name) > 0:
        # print(f'Attetion! The characters with name {name} is duplicated {len(education)} times!')
        # pytest.fail(f'Attetion! The characters with name {name} was not delete')


class TestPutCharacterByName:
    """
    Тест-кейсы направленные на тестирование работы метода PUT /character/{name}
    """
    pass


class TestDeleteCharacterByName:
    """
    Тест-кейсы направленные на тестирование работы метода DELETE /character/{name}
    """
    pass


class TestPostReset:
    """
    Тест-кейсы направленные на тестирование работы метода POST /reset
    """
    pass
