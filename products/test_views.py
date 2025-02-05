from django.test import TestCase
from .models import Product


class TestProductViews(TestCase):
    """ Test products views """
    def test_get_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')