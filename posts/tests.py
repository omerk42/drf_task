from django.contrib.auth.models import User
from posts.models import Post
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.


class DrfTaskTestCase(APITestCase):

    def Set_Up(self):
        # create test user
        self.user = User.objects.create_user(
            username='testusername',
            password='test_user_password',
            email='testuseremail@test.com'
        )
        # obtain jwt token for test user
        self.token = RefreshToken.for_user(self.user)
        self.access_token = str(self.token.access_token)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        # create posts
        Post.objects.create(user=User.objects.first(
        ), title="test post title 1", description="test post desc 1")
        Post.objects.create(user=User.objects.first(
        ), title="test post title 2", description="test post desc 2")

    def test_user_access_all_posts(self):
        '''
        test post list method
        '''
        response = self.client.get('/post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_access_own_post(self):
        '''
        test post list method
        '''
        user = User.objects.first()
        client = APIClient()
        client.force_authenticate(user=user)
        response = self.client.get('/post/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
