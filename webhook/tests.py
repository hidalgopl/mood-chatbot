from django.test import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .constants import VERIFY_TOKEN


class TestWebhook(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.webhook_url = reverse('webhook')

    def test_webhook_response(self):
        url = '{}?hub.verify_token={}'.format(self.webhook_url, VERIFY_TOKEN)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_request_response(self):
        url = '{}?=hub.verify_token={}'.format(self.webhook_url, 'bad_token')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
