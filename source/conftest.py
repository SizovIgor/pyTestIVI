# -*- coding: utf-8 -*-

"""
Файл фикстур, содержит в себе глобальные фикстуры всего проекта,
например такие, как создание объекта сессии `create_session`,
или обновление заголовков методов `post_setup`
"""
import pytest
import requests
from source.option import auth, proxies


@pytest.fixture(scope='module')
def create_session(request):
    """
    Глобавльная Фикстура для создания объекта сессии, с которым будут работать тесты.
    Вызывается для каждого модуля по отдельности

    :param request: фикстура py.Test, используется для отображения названия модуля для которого создается объект сессии
    :return: requests.Session
    """
    print(f'\nCreate Session() for module: {request.node.name}')
    global session
    session = requests.Session()
    session.trust_env = False
    session.proxies.update(proxies)
    session.auth = auth
    return session


@pytest.yield_fixture
def post_setup(create_session: requests.Session) -> None:
    """
    Фикстура по обновлению заголовков для методов, на уровне теста, где необходимо отправлять json на сервер.

    :return: None
    """
    create_session.headers['Content-type'] = 'Application/json'
    yield
    create_session.headers.pop('Content-type')
