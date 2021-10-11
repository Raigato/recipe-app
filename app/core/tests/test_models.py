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

    def test_new_user_email_normalized(self):
        """Tests that the email for a new user is normalized"""
        email = 'test@RAIGATO.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Tests that creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
