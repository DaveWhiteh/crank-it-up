from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


class TestProfileModels(TestCase):
    """ Test profile models """

    def setUp(self):
        """ Create objects for testing """

        # Test User
        testUser = User.objects.create_user(
            username="TestUser",
            password="Password123",
            email="test@test.com"
        )
        testUser.save()
        # Test Order Info
        testUser.userprofile.default_street_address1 = "Test Street Address 1"
        testUser.userprofile.default_street_address2 = "Test Street Address 2"
        testUser.userprofile.default_town_or_city = "Test City"
        testUser.userprofile.default_county = "Test County"
        testUser.userprofile.default_postcode = "42424"
        testUser.userprofile.default_country = "GB"
        testUser.userprofile.default_phone_number = "01234567890"
        testUser.userprofile.save()

    def test_profile_string_method(self):
        """ Test the string method on the profile model """
        test_user = User.objects.get(username='TestUser')
        profile = UserProfile.objects.get(user=test_user)
        self.assertEqual(str(profile), profile.user.username)

    def test_profile_info(self):
        """ Test the order address info """
        test_user = User.objects.get(username='TestUser')
        profile = UserProfile.objects.get(user=test_user)
        self.assertEqual(profile.default_street_address1, 'Test Street Address 1')
        self.assertEqual(profile.default_street_address2, 'Test Street Address 2')
        self.assertEqual(profile.default_town_or_city, 'Test City')
        self.assertEqual(profile.default_county, 'Test County')
        self.assertEqual(profile.default_postcode, '42424')
        self.assertEqual(profile.default_country, 'GB')
        self.assertEqual(profile.default_phone_number, '01234567890')