from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class HomePage(TestCase):
    
    def test_status_code(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)