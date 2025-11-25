from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        # Create a test user
        self.username = 'testuser'
        self.password = 'testpassword123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
        # The URL for the login page
        self.login_url = reverse('authentication:login')
        # The URL to redirect to on successful login
        self.success_url = reverse('main:show_main')

    def test_login_view_get(self):
        """Test that the login page loads correctly with a GET request."""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_successful_login(self):
        """Test a successful login with correct credentials."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        })
        
        # Check that the user is logged in
        self.assertTrue('_auth_user_id' in self.client.session)
        self.assertEqual(self.client.session['_auth_user_id'], str(self.user.id))
        
        # Check for the redirect to the main page
        self.assertRedirects(response, self.success_url)

    def test_unsuccessful_login_wrong_password(self):
        """Test a login attempt with an incorrect password."""
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': 'wrongpassword',
        })

        # Check that the user is NOT logged in
        self.assertFalse('_auth_user_id' in self.client.session)
        
        # Check that the page re-renders with an error
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please enter a correct username and password.")
