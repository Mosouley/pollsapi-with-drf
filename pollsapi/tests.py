from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.test import TestCase

from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from . import apiviews
from django.contrib.auth.models import User
from rest_framework import status

class TestPollsApi(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/pollsapi/'
# authentification of a user
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test', email='testuser@test.com', password='test'
        )

    def test_list(self):
        request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        # request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200, 
        'Espected Response Code 200, received {0} instead.'
        .format(response.status_code))

    
    def test_list2(self):
        #  login APIClient first
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200, 
        'Espected Response Code 200, received {0} instead.'
        .format(response.status_code))


    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you?",
            "created_by": self.user.id
        }
        response = self.client.post(self.uri, params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                    'Expected Response Code 201, received {0} instead.'
                    .format(response.status_code))