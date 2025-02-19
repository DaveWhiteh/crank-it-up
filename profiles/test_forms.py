from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForm(TestCase):
    """ Test profile forms """

    def test_profile_form(self):
        """ Test the profile form is valid with empty non required fields """
        form = UserProfileForm(
            {
                'default_phone_number': '',
                'default_street_address1': '',
                'default_street_address2': '',
                'default_town_or_city': '',
                'default_county': '',
                'default_postcode': '',
                'default_country': '',
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_form_has_placeholders(self):
        """ Test the profile form has placeholders """
        form = UserProfileForm()
        self.assertIn('placeholder="Phone Number"', form.as_p())
        self.assertIn('placeholder="Street Address 1"', form.as_p())
        self.assertIn('placeholder="Street Address 2"', form.as_p())
        self.assertIn('placeholder="Town or City"', form.as_p())
        self.assertIn('placeholder="County"', form.as_p())
        self.assertIn('placeholder="Postal Code"', form.as_p())