from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@raigato.com', password='Testpass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_create_new_superuser(self):
        "Tests creating a new superuser"
        user = get_user_model().objects.create_superuser('test@raigato.com', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


class TagModelTests(TestCase):
    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name='Vegan')

        self.assertEqual(str(tag), tag.name)
