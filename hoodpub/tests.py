from rest_framework import status
from rest_framework.test import APITestCase


class APITest(APITestCase):
    fixtures = ['users']

    def setUp(self):
        pass

    def test_userbook(self):
        url = '/api/userbook/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json()))
