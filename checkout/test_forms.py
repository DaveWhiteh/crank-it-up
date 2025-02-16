from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """ Test orders forms """

    def test_order_first_name_required(self):
        """ Test the order first name is a required field """
        form = OrderForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')
    
    def test_order_last_name_required(self):
        """ Test the order last name is a required field """
        form = OrderForm({'last_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors.keys())
        self.assertEqual(form.errors['last_name'][0], 'This field is required.')
    
    def test_order_email_required(self):
        """ Test the order email is a required field """
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
    
    def test_order_phone_number_required(self):
        """ Test the order phone number is a required field """
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0], 'This field is required.')
    
    def test_order_street_address_1_required(self):
        """ Test the order street address 1 is a required field """
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(form.errors['street_address1'][0], 'This field is required.')
    
    def test_order_town_or_city_required(self):
        """ Test the order town or city is a required field """
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(form.errors['town_or_city'][0], 'This field is required.')
    
    def test_order_country_required(self):
        """ Test the order country is a required field """
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['country'][0], 'This field is required.')