import base64

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


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
            'value': base64.b64encode(raw_data)
        }
        url = reverse('authenticate')

        response = self.client.post(
            url, data, format='json'
        )
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
