from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from .auth_utils import encode_credentials


class TestUserAuthentication(APITestCase):
    @classmethod
    def setUpClass(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            'testuser', 'test@user.com', 'test'
        )
        super(TestUserAuthentication, cls).setUpClass()

    def test_login(self):
        raw_data = '{}:{}'.format(self.user.username, 'test')
        data = {
            'auth': 'basic',
            'value': encode_credentials(raw_data)
        }
        url = reverse('authenticate')

        response = self.client.post(
            url, data, format='json'
        )
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()


class TestUserRegistration(APITestCase):
    def test_registration(self):
        data = {
            'username': 'testuser',
            'password': 'test',
            'email': 'test@user.com',
            'first_name': 'Po',
            'last_name': 'Panda',
        }
        url = reverse('register')

        response = self.client.post(
            url, data, format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('pk', response.data)
