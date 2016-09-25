from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class TestTenantRegistratoin(APITestCase):
    def test_registration(self):
        data = {
            'user': {
                'username': 'testuser',
                'password': 'test',
                'email': 'test@user.com',
                'first_name': 'Po',
                'last_name': 'Panda',
            }
        }
        url = reverse('tenants:register')

        response = self.client.post(
            url, data, format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('pk', response.data)
