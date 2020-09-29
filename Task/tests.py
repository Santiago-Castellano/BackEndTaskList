import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from Task.models import GroupTask, TypeTask, Task
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


class TaskTestCase(APITestCase):

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
        type_task = TypeTask(
            group=self.group,
            color="red",
            name="task red"
        )
        type_task.save()
        self.type_task = type_task

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")

     #Create
    def test_create_task_authenticated(self):
        data = {
            "to_do":"firs task",
        }
        response = self.client.post(reverse("create_task",kwargs={"pk_group":self.group.pk, "pk_type":self.type_task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_create_task_authenticated_and_not_found_group(self):
        data = {
            "to_do":"firs task",
        }
        response = self.client.post(reverse("create_task",kwargs={"pk_group":0, "pk_type":self.type_task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    
    def test_create_task_authenticated_and_not_found_type(self):
        data = {
            "to_do":"firs task",
        }
        response = self.client.post(reverse("create_task",kwargs={"pk_group":self.group.pk, "pk_type":0}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    
    def test_create_task_authenticated_and_un_autorized_group(self):
        new_user = User.objects.create_user(username="new_user",password="Aa_123456")
        new_group = GroupTask(
            user= new_user,
            name="new group"
        )
        new_group.save()
        data = {
            "to_do":"first task",
        }
        response = self.client.post(reverse("create_task",kwargs={"pk_group":new_group.pk, "pk_type":self.type_task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
    #UPDATE 
    def test_update_task_authenticated(self):
        task = Task(
            group=self.group,
            type_task=self.type_task,
            to_do="first task create"
        )
        task.save()
        data = {
            "to_do":"first task update",
        }
        response = self.client.put(reverse("update_task",kwargs={"pk":task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_task_authenticated_and_not_found_task(self):
        task = Task(
            group=self.group,
            type_task=self.type_task,
            to_do="first task create"
        )
        task.save()
        data = {
            "to_do":"first task update",
        }
        response = self.client.put(reverse("update_task",kwargs={"pk":0}),data)
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_update_task_un_authenticated(self):
        task = Task(
            group=self.group,
            type_task=self.type_task,
            to_do="first task create"
        )
        task.save()
        data = {
            "to_do":"first task update",
        }
        self.client.force_authenticate(user=None)
        response = self.client.put(reverse("update_task",kwargs={"pk":task.pk}),data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    #DELETE 
    def test_delete_task_authenticated(self):
        task = Task(
            group=self.group,
            type_task=self.type_task,
            to_do="first task create"
        )
        task.save()
        response = self.client.delete(reverse("delete_task",kwargs={"pk":task.pk}))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_task_authenticated_and_not_found_task(self):
        response = self.client.delete(reverse("delete_task",kwargs={"pk":0}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_delete_task_authenticated_and_un_autorized_group(self):
        new_user = User.objects.create_user(username="new_user",password="Aa_123456")
        new_group = GroupTask(
            user= new_user,
            name="new group"
        )
        new_group.save()
        task_type = TypeTask(
            name="type red",
            group=new_group,
            color="redddd"
        )
        task_type.save()
        task = Task(
            group=new_group,
            type_task=task_type,
            to_do="task new"
        )
        task.save()
        response = self.client.delete(reverse("delete_task",kwargs={"pk":task.pk}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

    def test_delete_task_un_authenticated(self):
        task = Task(
            group=self.group,
            type_task=self.type_task,
            to_do="first task create"
        )
        task.save()
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse("delete_task",kwargs={"pk":task.pk}))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)