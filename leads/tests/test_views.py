from django.test import TestCase
from django.shortcuts import reverse
from loguru import logger

# Create your tests here.
class LandingPageTest(TestCase):
    
    def test_status_code(self):
        # TODO some sort of test 
        response = self.client.get(reverse("landing_page"))
        self.assertEqual(response.status_code, 200)
        logger.info("Landing page status code is 200")
        self.assertTemplateUsed(response, "landing.html")
        logger.info("Landing page works correctly with template")
