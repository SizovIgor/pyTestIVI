import pytest
import requests

base_url = 'http://rest.test.ivi.ru{}'
characters = '/characters'
character = '/character'
characters_by_name = '/characters/{}'
character_by_name = '/character/{}'
reset = "/reset"

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


def ids(val):
    return f'api="{val[0]}"  code={val[1]}'


class TestAllowedMethods:

    @pytest.mark.parametrize("api_and_response", [
        ('/characters', 200),
        ('/character/Abyss', 200),
        ('/character', 405),
        ('/reset', 405)],
                             ids=ids
                             )
    def test_get_method(self, api_and_response):
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
    def test_post_method(self, post_setup, api_and_response):
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
    def test_put_method(self, post_setup, api_and_response):
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
    def test_delete_method(self, api_and_response):
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
    def test_options_method(self, api_and_response):
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
    def test_patch_method(self, api_and_response):
        api_method, expected_response_code = api_and_response
        response = session.put(
            url=base_url.format(api_method),
        )
        assert expected_response_code == response.status_code, f'Response error message:\n{response.text}'
