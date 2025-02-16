from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Category


class TestProductViews(TestCase):
    """ Test products views """

    def setUp(self):
        """ Create objects for testing """

        # Test User
        self.testUser = User.objects.create_user(
            username="TestUser",
            password="Password123"
        )
        # Test Superuser
        self.testSuperuser = User.objects.create_superuser(
            username="TestSuperuser",
            password="Password123"
        )
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
        """ Test getting the products page """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
    
    def test_get_product_detail_page_valid_product(self):
        """ Test getting the product detail page with a valid product """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
    
    def test_get_product_detail_page_invalid_product(self):
        """ Test getting the product detail page with an invalid product """
        response = self.client.get('/products/100/')
        self.assertEqual(response.status_code, 404)
    
    def test_sort_products(self):
        """ Test sorting products """
        # Sort by brand name
        response = self.client.get('/products/', {'sort': 'brand_name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        # Sort by category desc
        response = self.client.get('/products/', {'sort': 'category', 'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        # Sort by price
        response = self.client.get('/products/', {'sort': 'price'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
    
    def test_get_product_add_page_as_superuser(self):
        """ Test getting the product add page as a superuser """
        login = self.client.login(username="TestSuperuser", password="Password123")
        self.assertTrue(login)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')
    
    def test_get_product_add_page_as_user(self):
        """ Test getting the product add page as a user (Not a Superuser) """
        login = self.client.login(username="TestUser", password="Password123")
        self.assertTrue(login)
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_get_product_add_page_as_non_user(self):
        """ Test getting the product add page not logged in """
        response = self.client.get('/products/add/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/products/add/')
    
    def test_add_product_as_superuser(self):
        """ Test adding a product as a superuser """
        login = self.client.login(username="TestSuperuser", password="Password123")
        self.assertTrue(login)
        response = self.client.post('/products/add/', {
            'brand_name': 'Whyte',
            'model_name': "909",
            'description': "Test description",
            'size': "Small",
            'colour': "Blue",
            'price': 499.99,
            'is_featured': False,
            'is_active': True
        })
        self.assertRedirects(response, '/products/2/')
    
    def test_get_product_edit_page_as_superuser(self):
        """ Test getting the product edit page as a superuser """
        login = self.client.login(username="TestSuperuser", password="Password123")
        self.assertTrue(login)
        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')
    
    def test_get_product_edit_page_as_user(self):
        """ Test getting the product edit page as a user (Not a Superuser) """
        login = self.client.login(username="TestUser", password="Password123")
        self.assertTrue(login)
        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_get_product_edit_page_as_non_user(self):
        """ Test getting the product edit page not logged in """
        response = self.client.get('/products/edit/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/products/edit/1/')
    
    def test_edit_product_as_superuser(self):
        """ Test editing a product as a superuser """
        login = self.client.login(username="TestSuperuser", password="Password123")
        self.assertTrue(login)
        product = Product.objects.get()
        response = self.client.post(f'/products/edit/{product.id}/', {
            'brand_name': 'Update Brand Name',
            'model_name': "Update Model Name",
            'description': "Update Description",
            'size': "Medium",
            'colour': "Red",
            'price': 1.99,
            'is_featured': False,
            'is_active': True
        })
        product_updated = Product.objects.get()
        self.assertEqual(product_updated.brand_name, 'Update Brand Name')
    
    def test_get_product_delete_page_as_superuser(self):
        """ Test getting the product delete page as a superuser """
        login = self.client.login(username="TestSuperuser", password="Password123")
        self.assertTrue(login)
        response = self.client.get('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')
    
    def test_get_product_delete_page_as_user(self):
        """ Test getting the product delete page as a user (Not a Superuser) """
        login = self.client.login(username="TestUser", password="Password123")
        self.assertTrue(login)
        response = self.client.get('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
    
    def test_get_product_delete_page_as_non_user(self):
        """ Test getting the product delete page not logged in """
        response = self.client.get('/products/delete/1/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/products/delete/1/')
    
    def test_delete_product_as_superuser(self):
        """ Test deleting a product as a superuser """
        login = self.client.login(username="TestSuperuser", password="Password123")
        self.assertTrue(login)
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/')
        product_deleted = Product.objects.filter(id=product.id)
        self.assertEqual(len(product_deleted), 0)