"""
Файл фикстур, содержит в себе фикстуры для данной категории тестов.
"""
import pytest
import requests
from source.option import auth


@pytest.yield_fixture(scope='module')
def delete_auth(create_session: requests.Session):
    create_session.auth = None
    print('\nAuth was deleted')
    yield
    create_session.auth = auth
    print('\nAuth was restored')
