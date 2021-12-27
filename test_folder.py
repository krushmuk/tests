import unittest
import app_2
import requests

token = str


class TestAddFolder(unittest.TestCase):
    def test_new_folder(self):
        self.assertEqual(app_2.create_folder(token, 'new_folder').status_code, 201)
        existence = requests.get(url=app_2.url, headers={'content type': 'application/json',
                                                        'authorization': f'OAuth {token}'},
                                 params={'path': 'new_folder'})
        self.assertEqual(existence.status_code, 200)
