from django.test import TestCase
from .models import Product, Category


class TestProductModels(TestCase):
    """ Test products models """

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
    
    def test_category_string_method(self):
        """ Test the string method on the category model """
        category = Category(name='TestCategoryName', friendly_name='Test Category Name')
        self.assertEqual(str(category), category.name)
        self.assertEqual(str(category.friendly_name), category.friendly_name)
    
    def test_product_string_method(self):
        """ Test the string method on the product model """
        product = Product(model_name='Clockwork')
        self.assertEqual(str(product), product.model_name)
    
    def test_category_name(self):
        """ Test the category name """
        self.assertEqual(self.testCategory.name, 'TestCategory')
    
    def test_category_friendly_name(self):
        """ Test the category friendly name """
        self.assertEqual(self.testCategory.friendly_name, 'Test Category')
    
    def test_product_brand_name(self):
        """ Test the product brand name """
        self.assertEqual(self.testProduct.brand_name, 'Orange')
    
    def test_product_model_name(self):
        """ Test the product model name """
        self.assertEqual(self.testProduct.model_name, 'Clockwork')
    
    def test_product_description(self):
        """ Test the product description """
        self.assertEqual(self.testProduct.description, 'Test description')
    
    def test_product_size(self):
        """ Test the product size """
        self.assertEqual(self.testProduct.size, 'Large')
    
    def test_product_colour(self):
        """ Test the product colour """
        self.assertEqual(self.testProduct.colour, 'Green')
    
    def test_product_price(self):
        """ Test the product price """
        self.assertEqual(self.testProduct.price, 99.99)
    
    def test_product_is_featured(self):
        """ Test the product is featured """
        self.assertFalse(self.testProduct.is_featured)
    
    def test_product_is_active(self):
        """ Test the product is active """
        self.assertTrue(self.testProduct.is_active)