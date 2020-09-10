import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from Task.views.group_task import create, delete, detail, update
from Task.serializers import GroupTaskSerializer

class GroupTaskTestCase(APITestCase):

    url_create = reverse("create_group_task")
    
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass-123456")
        self.token = Token.objects.get(user=self.user).key
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
    
    def test_create_group_task_authenticated(self):
        data = {
            "name":"new group of task"
        }
        response = self.client.post(self.url_create,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_create_group_task_un_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "name":"new group of task"
        }
        response = self.client.post(self.url_create,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    