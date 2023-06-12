from django.test import TestCase

# Create your tests here.
from .views import home



#Test that requesting the homepage (/) returns a 200 success status code

class HomePageTest (TestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

