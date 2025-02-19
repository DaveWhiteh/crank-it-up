from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order


class TestProfileViews(TestCase):
    """ Test profile views """

    def setUp(self):
        """ Create objects for testing """

        # Test User
        testUser = User.objects.create_user(
            username="TestUser",
            password="Password123",
            email="test@test.com"
        )
        testUser.save()
        # Test Order
        Order.objects.create(
            order_number="12345",
            user_profile=UserProfile.objects.get(user=testUser),
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

    def test_get_profile_page(self):
        """ Test getting to user profile page """
        self.client.login(username='TestUser', password="Password123")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
    
    def test_post_profile_page(self):
        """ Test getting to user profile page """
        self.client.login(username='TestUser', password="Password123")
        response = self.client.post('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_get_order_history(self):
        """ Test getting the order history """
        self.client.login(username='TestUser', password="Password123")
        test_user = User.objects.get(username='TestUser')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get('/profile/order_history/' + order.order_number)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')