import pytest
import requests
from source.option import auth, proxies


@pytest.fixture(scope='module')
def create_session(request):
    print(f'Create Session() for module: {request.node.name}')
    global session
    session = requests.Session()
    session.trust_env = False
    session.proxies.update(proxies)
    session.auth = auth
    return session


@pytest.yield_fixture(scope='module')
def delete_auth(create_session: requests.Session):
    create_session.auth = None
    print('Auth was deleted')
    yield
    create_session.auth = auth
    print('Auth was restored')


@pytest.yield_fixture
def post_setup(create_session: requests.Session) -> None:
    """
    Фикстура по обновлению заголовков для методов, на уровне теста, где необходимо отправлять json на сервер.

    :return: None
    """
    create_session.headers['Content-type'] = 'Application/json'
    yield
    create_session.headers.pop('Content-type')
