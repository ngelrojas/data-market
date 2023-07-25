from datetime import datetime
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

MARKET_URL = reverse('market_yfi_recovery:market')


class MarketApiTests(TestCase):
    """Test the market API"""

    def setUp(self):
        self.client = APIClient()

    def test_filter_by_date_range(self):

        data = {
            'start_date': '2012-05-18',
            'end_date': '2012-06-18'
        }
        response = self.client.get(MARKET_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missing_date_parameters(self):
        response = self.client.get(MARKET_URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error = {"error": "start_date and end_date are required"}
        self.assertEqual(response.data, expected_error)
