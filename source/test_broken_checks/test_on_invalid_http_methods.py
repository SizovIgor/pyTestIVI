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
    session.headers['Content-type'] = 'Application/json'

    def resource_teardown():
        session.headers.pop('Content-type')

    request.addfinalizer(resource_teardown)


# @pytest.mark.skip
def ptest_get_characters():
    response = session.get(base_url.format(characters))
    print(
        '\nstatus_code: ', response.status_code,
        '\nreason: ', response.reason,
        '\ntext: ', response.text,
        response
    )
    assert response.ok


#
# @pytest.fixture(scope="class", params=[
# ("abcdefg", "abcdefg?"),
# ("abc", "abc!"),
# ("abcde", "abcde.")],
# )
# def param_test_idfn(request):
#     return request.param
def ids(val):
    return f'api="{val[0]}"  code={val[1]}'


class TestGetCharacters:

    @pytest.mark.parametrize("api_and_response", [
        ('/characters', 405),
        ('/character/Abyss', 405),
        ('/character', 200),
        ('/reset', 200)],
                             ids=ids
                             )
    def test_post_method(self, resource_setup, api_and_response):
        api_method, expected_response_code = api_and_response
        # print(
        #     f'\nMethod: POST\nAPI: {api_method}\nExpected response code: {expected_response_code}\nResult: '
        # )
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

    def test_put_method(self):
        # session.put(base_url.format(characters))
        pass

    def test_delete_method(self):
        # session.delete(base_url.format(characters))
        pass

    def test_options_method(self):
        # session.options(base_url.format(characters))
        pass

    def test_patch_method(self):
        # session.patch(base_url.format(characters))
        pass
