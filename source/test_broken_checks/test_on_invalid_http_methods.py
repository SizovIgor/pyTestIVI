# -*- coding: utf-8 -*-

"""
Проверки коректности ответа от сервера на запросы различными HTTP-методами

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


def ids(val) -> str:
    """
    Метод форатирующий строку в удобочитаемый вид, для отображения в консоли при выполнении тестов.
    Поскольку тесты запускаются с множеством различных параметров, то необходимо понимать на каком
    из сочетании входных параметров тест падает (или наоборот, проходит)

    :param val: список параметров, которые будут переданы в тест
    :return str: готовая отформатированная строка
    """
    return f'api="{val[0]}"  code={val[1]}'


@pytest.mark.parametrize("api_and_response", [
    ('/characters', 200),
    ('/character/Abyss', 200),
    ('/character', 405),
    ('/reset', 405)],
                         ids=ids
                         )
def test_get_method(api_and_response):
    """
    Параметризованный тест, направленный на проверку доступности http-метода GET ко всем API-методам

    :param api_and_response: кортеж, состоящий из ссылки на API-метод и ожидаемого статуса-кода ответа
    :return: Fail/Pass
    """
    api_method, expected_response_code = api_and_response
    response = session.get(
        url=base_url.format(api_method),
    )
    assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'


@pytest.mark.parametrize("api_and_response", [
    ('/characters', 405),
    ('/character/Abyss', 405),
    ('/character', 200),
    ('/reset', 200)],
                         ids=ids
                         )
def test_post_method(post_setup, api_and_response):
    """
    Параметризованный тест, направленный на проверку доступности http-метода POST ко всем API-методам

    :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
    :param api_and_response: кортеж, состоящий из ссылки на API-метод и ожидаемого статуса-кода ответа
    :return: Fail/Pass
    """
    api_method, expected_response_code = api_and_response
    payload = {
        "name": "xxx_777",
        "universe": "xxx_7771",
        "education": "xxx_7772",
        "weight": 777,
        "height": 7.71,
        "identity": "xxx_7773",
        "other_aliases": "None"
    }
    response = session.post(
        url=base_url.format(api_method),
        json=payload
    )
    assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'


@pytest.mark.parametrize("api_and_response", [
    ('/characters', 405),
    ('/character/Abyss', 200),
    ('/character', 405),
    ('/reset', 405)],
                         ids=ids
                         )
def test_put_method(post_setup, api_and_response):
    """
    Параметризованный тест, направленный на проверку доступности http-метода PUT ко всем API-методам

    :param post_setup: вызов фикстуры, для подготовки заголовков, для отправки json на сервер
    :param api_and_response: кортеж, состоящий из ссылки на API-метод и ожидаемого статуса-кода ответа
    :return: Fail/Pass
    """
    api_method, expected_response_code = api_and_response
    payload = {
        "name": "Abyss",
        "universe": "xxx_7771",
        "education": "xxx_7772",
        "weight": 777,
        "height": 7.71,
        "identity": "xxx_7773",
        "other_aliases": "None"
    }
    response = session.put(
        url=base_url.format(api_method),
        json=payload
    )
    assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'


@pytest.mark.parametrize("api_and_response", [
    ('/characters', 405),
    ('/character/Abyss', 200),
    ('/character', 405),
    ('/reset', 405)],
                         ids=ids
                         )
def test_delete_method(api_and_response):
    """
    Параметризованный тест, направленный на проверку доступности http-метода DELETE ко всем API-методам

    :param api_and_response: кортеж, состоящий из ссылки на API-метод и ожидаемого статуса-кода ответа
    :return: Fail/Pass
    """
    api_method, expected_response_code = api_and_response
    response = session.delete(
        url=base_url.format(api_method),
    )
    assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'


@pytest.mark.parametrize("api_and_response", [
    ('/characters', 200),
    ('/character/Abyss', 200),
    ('/character', 200),
    ('/reset', 200)],
                         ids=ids
                         )
def test_options_method(api_and_response):
    """
    Параметризованный тест, направленный на проверку доступности http-метода OPTIONS ко всем API-методам

    :param api_and_response: кортеж, состоящий из ссылки на API-метод и ожидаемого статуса-кода ответа
    :return: Fail/Pass
    """
    api_method, expected_response_code = api_and_response
    response = session.options(
        url=base_url.format(api_method),
    )
    assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'


@pytest.mark.parametrize("api_and_response", [
    ('/characters', 405),
    ('/character/Abyss', 405),
    ('/character', 405),
    ('/reset', 405)],
                         ids=ids
                         )
def test_patch_method(api_and_response):
    """
    Параметризованный тест, направленный на проверку доступности http-метода PATCH ко всем API-методам

    :param api_and_response: кортеж, состоящий из ссылки на API-метод и ожидаемого статуса-кода ответа
    :return: Fail/Pass
    """
    api_method, expected_response_code = api_and_response
    response = session.put(
        url=base_url.format(api_method),
    )
    assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'
