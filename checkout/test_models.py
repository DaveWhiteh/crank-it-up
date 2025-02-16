from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product, Category


class TestCheckoutModels(TestCase):
    """ Test checkout models """

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
        self.testOrder = Order.objects.create(
            order_number='123',
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

        self.testOrderLineItem1 = OrderLineItem.objects.create(
            order=self.testOrder,
            product=self.testProduct,
        )
    
    def test_order_string_method(self):
        """ Test the string method on the order model """
        order = Order(order_number='123')
        self.assertEqual(str(order), order.order_number)

    def test_order_number(self):
        """ Test the order number """
        self.assertEqual(self.testOrder.order_number, '123')

    def test_order_first_name(self):
        """ Test the order first name """
        self.assertEqual(self.testOrder.first_name, 'Test Firstname')
    
    def test_order_last_name(self):
        """ Test the order last name """
        self.assertEqual(self.testOrder.last_name, 'Test Lastname')

    def test_order_email(self):
        """ Test the order email """
        self.assertEqual(self.testOrder.email, 'test@test.com')

    def test_order_phone(self):
        """ Test the order phone """
        self.assertEqual(self.testOrder.phone_number, '01234567890')
    
    def test_order_street_address_1(self):
        """ Test the order street address 1 """
        self.assertEqual(self.testOrder.street_address1, 'Test Street Address 1')
    
    def test_order_street_address_2(self):
        """ Test the order street address 2 """
        self.assertEqual(self.testOrder.street_address2, 'Test Street Address 2')
    
    def test_order_town_or_city(self):
        """ Test the order town or city """
        self.assertEqual(self.testOrder.town_or_city, 'Test City')
    
    def test_order_county(self):
        """ Test the order county """
        self.assertEqual(self.testOrder.county, 'Test County')
    
    def test_order_country(self):
        """ Test the order country """
        self.assertEqual(self.testOrder.country, 'GB')