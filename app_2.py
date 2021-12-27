import requests
url = 'https://cloud-api.yandex.net/v1/disk/resources'


def create_folder(token, folder):
    headers = {'content type': 'application/json',
               'authorization': f'OAuth {token}'}
    params = {'path': folder}
    created_folder = requests.put(url=url, headers=headers, params=params)
    return created_folder
