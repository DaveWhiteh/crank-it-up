from django.test import TestCase
from .models import Order
from products.models import Product, Category


class TestBagViews(TestCase):
    """ Test checkout views """

    def setUp(self):
        """ Create objects for testing """

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
        # Test Order
        self.order = Order.objects.create(
            first_name="Test Firstname",
            last_name="Test Lastname",
            email="test@test.com",
            phone_number="01234567890",
            street_address1="Test Street Address 1",
            street_address2="Test Street Address 2",
            town_or_city="Test City",
            county="Test County",
            country="GB",
        )
    
    def test_get_checkout_page_empty_bag(self):
        """ Test redirecting to products page from checkout with empty bag """
        response = self.client.get('/checkout/')
        self.assertTrue(response, '/products')
        self.assertRedirects(response, '/products/')