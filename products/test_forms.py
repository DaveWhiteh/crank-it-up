from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """ Test products forms """

    def test_product_brand_name_required(self):
        """ Test the product brand name is a required field """
        form = ProductForm({'brand_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('brand_name', form.errors.keys())
        self.assertEqual(form.errors['brand_name'][0], 'This field is required.')
    
    def test_product_model_name_required(self):
        """ Test the product model name is a required field """
        form = ProductForm({'model_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('model_name', form.errors.keys())
        self.assertEqual(form.errors['model_name'][0], 'This field is required.')
    
    def test_product_description_required(self):
        """ Test the product description is a required field """
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')
    
    def test_product_size_required(self):
        """ Test the product size is a required field """
        form = ProductForm({'size': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('size', form.errors.keys())
        self.assertEqual(form.errors['size'][0], 'This field is required.')
    
    def test_product_colour_required(self):
        """ Test the product colour is a required field """
        form = ProductForm({'colour': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('colour', form.errors.keys())
        self.assertEqual(form.errors['colour'][0], 'This field is required.')
    
    def test_product_price_required(self):
        """ Test the product price is a required field """
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')
    
    def test_product_form(self):
        """ Test the product form is valid with empty non required fields """
        form = ProductForm(
            {
                'category': '',
                'brand_name': 'Test Brand Name',
                'model_name': 'Test Model Name',
                'description': 'Test Description',
                'size': 'Test Size',
                'colour': 'Test Colour',
                'price': '20.99',
                'is_featured': '',
                'is_active': '',
                'image': '',
            }
        )
        self.assertTrue(form.is_valid())