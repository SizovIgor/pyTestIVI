
import pytest
import requests

# from wemake_python_styleguide.violations.best_practices import (
#     NegatedConditionsViolation,
# )
# from wemake_python_styleguide.visitors.ast.conditions import IfStatementVisitor


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
def resource_setup(request):
    print('Change content-type')
    session.headers['Content-type'] = 'Application/json'

    def resource_teardown():
        print('Return content-type')
        session.headers.pop('Content-type')

    request.addfinalizer(resource_teardown)


# @pytest.mark.skip
def test_get_characters():
    response = session.get(base_url.format(characters))
    print(
        '\nstatus_code: ', response.status_code,
        '\nreason: ', response.reason,
        '\ntext: ', response.text,
        response
    )
    assert response.ok
