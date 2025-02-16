from django.test import TestCase
from products.models import Product, Category

from django.test import Client


class TestBagViews(TestCase):
    """ Test bag views """

    def setUp(self):
        """ Create objects for testing """

        self.client = Client()

        # Test Category
        self.testCategory = Category.objects.create(
            name="TestCategory",
            friendly_name="Test Category",
        )
        # Test Product
        self.testProduct = Product.objects.create(
            category=self.testCategory,
            brand_name="Orange",
            model_name="Clockwork",
            description="Test description",
            size="Large",
            colour="Green",
            price=99.99,
            is_featured=False,
            is_active=True
        )
    
    def test_get_products_page(self):
        """ Test getting the bag page """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')