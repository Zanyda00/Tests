import requests


class Yandex:
    base_host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Authorization': f'OAuth {self.token}'}

    def create_folder(self, path):
        uri = f'/v1/disk/resources?path={path}'
        request_url = self.base_host + uri
        response = requests.put(request_url, headers=self.get_headers())
        return response.status_code


if __name__ == '__main__':
    token = 'y0_AgAAAAAiKjK1AADLWwAAAADWfZKpr-nFuuQFSGCezUy2_d5pJLtaMAQ'
    Ya = Yandex(token)
    Ya.create_folder(...)
