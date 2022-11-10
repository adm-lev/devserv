from typing import NoReturn
import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User as UserModel
from todos.views import UserCustomViewSet
from todos.models import User, Project, Todo
from rest_framework.authtoken.models import Token

class TestUserViewSet(TestCase):

    def setUp(self) -> None :
        self.url: str = '/api/users/'
        self.data: dict = {'user_name': 'guest', 'first_name':'Alex',
                    'last_name': 'Bolduin', 'email': 'ab@mail.co'}
        self.data_put: dict = {'user_name': 'guest1', 'first_name':'Alex1', 
                    'last_name': 'Bolduin1', 'email': 'ab1@mail.co'}        
        self.login = {
            'username': 'admin',
            'password': 'admin_123456'
        }
        self.admin: object = UserModel.objects.create_superuser('admin', 'admin@admin.com',
         'admin_123456')
        


    # def test_get_list(self):

    #     factory = APIRequestFactory()
    #     request = factory.get(self.url)
    #     view = UserCustomViewSet.as_view({'get': 'list'})
    #     response = view(request)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_create_guest(self):

    #     factory = APIRequestFactory()
    #     request = factory.post(self.url, self.data, format='json')
    #     view = UserCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)

    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # def test_create_admin(self):

    #     factory = APIRequestFactory()
    #     request = factory.post(self.url, self.data, format='json')        
    #     force_authenticate(request, self.admin)
    #     view = UserCustomViewSet.as_view({'post': 'create'})
    #     response = view(request)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    # def test_get_detail(self):

    #     client = APIClient()
    #     user = User.objects.create(**self.data)        
    #     response = client.get(f'{self.url}{user.id}/')   

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


    # def test_edit_guest(self):

    #     user = User.objects.create(**self.data)       
    #     client = APIClient()
    #     response = client.put(f'{self.url}{user.id}/', self.data_put, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



    # def test_edit_admin(self):
       
    #     user = User.objects.create(**self.data) 
    #     client = APIClient()                 
    #     client.login(username='admin',password='admin_123456')
    #     response = client.put(f'{self.url}{user.id}/', self.data_put)
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     user_update = User.objects.get(id=user.id)
    #     self.assertEqual(user_update.user_name, 'guest1')
    #     self.assertEqual(user_update.first_name, 'Alex1')
    #     client.logout()

    def tearDown(self) -> NoReturn:
        pass


class TestProjectViewSet(APITestCase):

    def setUp(self) -> None:
            
        self.url: str = '/api/projects/'
        self.name = 'admin'
        self.password = 'password'
        self.admin = UserModel.objects.create_superuser(self.name, 'email@email.com', self.password)
        self.admin2 = UserModel.objects.create_superuser('admin2','admin2@mail.ru','admin2')
        self.data: dict = {'user_name': 'guest', 'first_name':'Alex',
                    'last_name': 'Bolduin', 'email': 'ab@mail.co'}
        self.data_put: dict = {'user_name': 'guest1', 'first_name':'Alex1', 
                    'last_name': 'Bolduin1', 'email': 'ab1@mail.co'}


    # def test_get_projects(self):

    #     request = self.client.get(self.url)
    #     self.assertEqual(request.status_code, status.HTTP_200_OK)
        

    
    # def test_create_project(self):

    #     user = User.objects.create(**self.data)
    #     # token = Token.objects.get(user__username='admin')
    #     self.client.login(username=self.name,password=self.password)
    #     # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    #     response = self.client.put(f'{self.url}{user.id}/', self.data_put, format='json')
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.client.logout()

    def test_edit_mixer(self):

        proj = mixer.blend(Project)

        self.client.login(username='admin2',password='admin2')

        response = self.client.put(f'{self.url}{proj.id}/', {'name':'testtest','project_url':'qwerty'}, format='json')
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    


