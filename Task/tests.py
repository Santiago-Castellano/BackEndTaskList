import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from Task.models import GroupTask, TypeTask
from Task.serializers import GroupTaskSerializer, TypeTaskSerializer


class GroupTaskTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass-123456")
        self.token = Token.objects.get(user=self.user).key
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
    
    #Create
    def test_create_group_task_authenticated(self):
        data = {
            "name":"new group of task"
        }
        response = self.client.post(reverse("create_group_task"),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_create_group_task_un_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "name":"new group of task"
        }
        response = self.client.post(reverse("create_group_task"),data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    #Detail
    def test_detail_group_task_authenticated(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        response = self.client.get(reverse("detail_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_detail_group_task_authenticated_not_found(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        response = self.client.get(reverse("detail_group_task",kwargs={"pk":0}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_detail_group_task_authenticated_not_have_permits(self):
        new_user = User.objects.create_user(username="new_user", password="pass-123456")
        group = GroupTask(
            user=new_user,
            name="group task new user"
        )
        group.save()
        response = self.client.get(reverse("detail_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_detail_group_task_un_authenticated(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse("detail_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    #Delete
    def test_delete_group_task_authenticated(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        response = self.client.delete(reverse("delete_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_group_task_authenticated_not_found(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        response = self.client.delete(reverse("delete_group_task",kwargs={"pk":0}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_delete_group_task_authenticated_not_have_permits(self):
        new_user = User.objects.create_user(username="new_user", password="pass-123456")
        group = GroupTask(
            user=new_user,
            name="group task new user"
        )
        group.save()
        response = self.client.delete(reverse("delete_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_delete_group_task_un_authenticated(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse("delete_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    #UPDATE
    def test_update_group_task_authenticated(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        data = {
            "name":"group task edit"
        }
        response = self.client.put(reverse("update_group_task",kwargs={"pk":group.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_group_task_authenticated_not_found(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        data = {
            "name":"group task edit"
        }
        response = self.client.put(reverse("update_group_task",kwargs={"pk":0}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_delete_group_task_authenticated_not_have_permits(self):
        new_user = User.objects.create_user(username="new_user", password="pass-123456")
        group = GroupTask(
            user=new_user,
            name="group task new user"
        )
        group.save()
        data = {
            "name":"group task edit"
        }
        response = self.client.put(reverse("update_group_task",kwargs={"pk":group.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_update_group_task_authenticated_and_not_have_data(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        data = {
            "name":"group task edit"
        }
        response = self.client.put(reverse("update_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_update_group_task_un_authenticated(self):
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse("update_group_task",kwargs={"pk":group.pk}))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)




class TypeTaskTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass-123456")
        self.token = Token.objects.get(user=self.user).key
        self.api_authentication()
        group = GroupTask(
            user=self.user,
            name="group task"
        )
        group.save()
        self.group = group

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
    
    #Create
    def test_create_type_task_authenticated(self):
        data = {
            "name":"firs task",
            "color":"red",
        }
        response = self.client.post(reverse("create_type_task",kwargs={"pk_group":self.group.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
         
    def test_create_type_task_authenticated_and_faild_group(self):
        data = {
            "name":"firs task",
            "color":"red",
        }
        response = self.client.post(reverse("create_type_task",kwargs={"pk_group":9}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
         

    def test_create_type_task_un_authenticated(self):
        data = {
            "name":"firs task",
            "color":"red",
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse("create_type_task",kwargs={"pk_group":self.group.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    #DETAIL
    def test_detail_type_task_authenticated(self):
        type_task = TypeTask(
            group=self.group,
            name="group task"
        )
        type_task.save()
        response = self.client.get(reverse("detail_type_task",kwargs={"pk":type_task.pk}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_detail_type_task_authenticated_not_found(self):
        response = self.client.get(reverse("detail_type_task",kwargs={"pk":0}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_detail_type_task_authenticated_not_have_permits(self):
        new_user = User.objects.create_user(username="new_user", password="pass-123456")
        group = GroupTask(
            user=new_user,
            name="group task new user"
        )
        group.save()
        type_task = TypeTask(group=group, name="tarea roja",color="red")
        type_task.save()
        response = self.client.get(reverse("detail_type_task",kwargs={"pk":type_task.pk}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_detail_task_task_un_authenticated(self):
        type_task = TypeTask(
            group=self.group,
            name="group task"
        )
        type_task.save()

        self.client.force_authenticate(user=None)
        response = self.client.get(reverse("detail_type_task",kwargs={"pk":type_task.pk}))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
   

   #UPDATE
    def test_update_type_task_authenticated(self):
        type_task = TypeTask(
            group=self.group,
            color="red",
            name="tipo rojo"
        )
        type_task.save()
        data = {
            "name":"tipo azul",
            "color":"blue"
        }
        response = self.client.put(reverse("update_type_task",kwargs={"pk":type_task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_task_task_authenticated_not_found(self):
        type_task = TypeTask(
            group=self.group,
            color="red",
            name="tipo rojo"
        )
        type_task.save()
        data = {
            "name":"tipo azul",
            "color":"blue"
        }
        response = self.client.put(reverse("update_type_task",kwargs={"pk":0}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_delete_group_task_authenticated_not_have_permits(self):
        new_user = User.objects.create_user(username="new_user", password="pass-123456")
        group = GroupTask(
            user=new_user,
            name="group task new user"
        )
        group.save()
        type_task = TypeTask(
            group=group,
            color="red",
            name="tipo rojo"
        )
        type_task.save()
    
        data = {
            "name":"tipo azul",
            "color":"blue"
        }
        response = self.client.put(reverse("update_type_task",kwargs={"pk":type_task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    #DELETE
    def test_delete_type_task_authenticated(self):
        type_task = TypeTask(
            name="group task",
            group=self.group,
            color="red"
            
        )
        type_task.save()
        response = self.client.delete(reverse("delete_type_task",kwargs={"pk":type_task.pk}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
   
    def test_delete_type_task_authenticated_not_found(self):
        response = self.client.delete(reverse("delete_type_task",kwargs={"pk":0}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_delete_group_task_authenticated_not_have_permits(self):
        new_user = User.objects.create_user(username="new_user", password="pass-123456")
        group = GroupTask(
            user=new_user,
            name="group task new user"
        )
        group.save()
        type_task = TypeTask(
            group=group,
            name="tarea nueva",
            color="red"
        )
        type_task.save()
        response = self.client.delete(reverse("delete_type_task",kwargs={"pk":type_task.pk}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
    
    def test_delete_type_task_un_authenticated(self):
        type_task = TypeTask(
            group=self.group,
            name="type task",
            color="red"
        )
        type_task.save()
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse("delete_type_task",kwargs={"pk":type_task.pk}))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)