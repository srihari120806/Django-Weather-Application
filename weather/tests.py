from django.test import TestCase
from django.urls import reverse

class WeatherPageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
