from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class LoginTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        # Send a POST request to the login endpoint with valid credentials
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        # Assert that the response status code is 200 or a redirect (successful login)
        self.assertIn(response.status_code, [200, 301, 302])
        # Optionally, assert that the user is now authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_failure(self):
        # Send a POST request to the login endpoint with invalid credentials
        response = self.client.post(reverse('login'), {'username': 'invalid', 'password': 'invalid'})
        # Assert that the response status code is 4xx (failed login)
        self.assertGreaterEqual(response.status_code, 400)
        # Optionally, assert that the user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)
