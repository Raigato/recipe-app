from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):
    def test_creates_user_with_email_successfully(self):
        """It creates a new user with an email successfully"""
        email = 'test@raigato.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
