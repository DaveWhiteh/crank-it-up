from django.test import TestCase


class TestHomeViews(TestCase):
    """ Test Home Views """
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')