from django.urls import reverse
from rest_framework.test import APITestCase


class TestApi(APITestCase):
    def test_get(self):
        url = reverse('books-list')
        print(url)
        responce = self.client.get(url)
        print(responce)
