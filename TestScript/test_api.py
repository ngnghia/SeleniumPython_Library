import json
import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Library.APIs import APICall


def test_api_get_user():
    url = "https://reqres.in/api/users/4"
    reponse = APICall().call_API_load(url)
    try:
        assert reponse['data']['email'] == "eve.holt@reqres.in"  # , "email is wrong"
        assert reponse['status'] == 200
    except Exception as e:
        print(e)


def test_api_add_user():
    lib = APICall()
    url = "https://reqres.in/api/register"
    payload = json.dumps({
        "email": "eve.holt@reqres.in",
        "password": "secret"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    print(lib.call_API_Add(url, headers, payload))
