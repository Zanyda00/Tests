import pytest
import requests
from main import Yandex

token = 'y0_AgAAAAAiKjK1AADLWwAAAADWfZKpr-nFuuQFSGCezUy2_d5pJLtaMAQ'


@pytest.mark.parametrize('exp', [200, 400])
def test_status_code(exp):
    response = requests.get('https://cloud-api.yandex.net:443')
    assert response.status_code == exp
    assert response.status_code == exp


def test_authorization():
    result = Yandex(token).create_folder(path='44')
    assert result == 401


def test_status_code_create_folder():
    result = Yandex(token).create_folder(path='44')
    assert result == 409
