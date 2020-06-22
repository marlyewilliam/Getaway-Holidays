from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from django.contrib.auth.models import User


class ClientTests(APITestCase):
    def test_create_client(self):
        
        url = '/users/'
        data = {
            "email": "marlywilliam31@gmail.com",
            "username": "test1234",
            "first_name": "Marly",
            "last_name": "Last",
            "password": "password123",
                "profile": {
                "address": "8 Abu Obeid Ebn El Garrah St. Al Shams Club, Heliopolis, Cairo",
                "state": "Cairo",
                "postcode": "11234",
                "contact_number": "01222717592",
                "occupation": "Back-end Developer",
                "marital_status": "Single",
                "gender": "Female",
                "city": "cairo",
                "birthday": "1997-01-31",
                "client_signature": "Marly Emad William",
                "signature_date": "2020-06-17T12:23:32Z",
                "created_date": "2020-06-21T11:08:15.197144Z",
                "updated_date": "2020-06-21T11:08:15.211385Z",
                "health_conditions": {
                    1,
                    2
                }
            }
        }
        HealthConditions.objects.create(name = 'Blood pressure')
        HealthConditions.objects.create(name = 'Heart condition')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().first_name, 'Marly')


    def test_get_clients(self):
        url = '/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_update_clients(self):
        url = '/users/'
        user = User.objects.create(email = "marlywilliam31@gmail.com",
            username = "test1234",
            first_name = "Marly",
            last_name = "Last",
            password = "password123")
        data = {'username' : 'testupdate'}
        url = url + str(user.id) +"/"
        response = self.client.patch(url, data, format='json') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.get().username, 'testupdate')

    def test_delete_clients(self):
        url = '/users/'
        user = User.objects.create(email = "marlywilliam31@gmail.com",
            username = "test1234",
            first_name = "Marly",
            last_name = "Last",
            password = "password123")
        url = url + str(user.id) +"/"
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
