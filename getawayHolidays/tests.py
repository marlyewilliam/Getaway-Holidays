from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from datetime import datetime, timedelta
from rest_framework.test import APIClient
from djmoney.money import Money
    


def get_user():
    user = User.objects.create(email = "marlywilliam31@gmail.com",
        username = "test1234",
        first_name = "Marly",
        last_name = "Emad",
        password = "password123")
    return user


def get_user2():
    user = User.objects.create(email = "marlywilliam31@gmail.com",
        username = "test2",
        first_name = "Merola",
        last_name = "Emad",
        password = "password123")
    return user

def get_accommodations():
    accommodation = Accommodations.objects.create(Name = "Honeymoon Cottage", 
    description = "perfect accommodations for couples",
    people_per_room = 2,
    number_of_rooms = 20,
    price_per_day = Money("20", "USD")
    )
    
    return accommodation

def get_activity():
    activity = Activities.objects.create(Name = "Hot Air Balloon Ride",
    description = "Take a ride above the horizon to discover the scenic beauty from a unique angle nothing else can provide.",
    activity_type = "Outdoor",
    risk_level = 'Medium',
    duration = '2:00:00',
    price_per_duration = Money("10", "USD")
    )
    return activity

def create_reservation():
    start_date = datetime.now() + timedelta(days=20)
    end_date = start_date + timedelta(days=5)
    # start_date = start_date.strftime("%Y-%m-%d")
    # end_date = end_date.strftime("%Y-%m-%d")
    user = get_user()
    accommodation =  get_accommodations()
    activity1 = get_activity()
    activity2 = get_activity()

    reservation = Reservations.objects.create(
        user = user,
        start_date = start_date,
        end_date = end_date,
        number_of_rooms = 2,
        client_signature = "Marly Emad William",
        signature_date = "2020-06-23T14:14:46Z",
        updated_date = "2020-06-23T14:15:43.716130Z",
        accommodations = accommodation
    )
    return reservation


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


class CreateReservationTests(APITestCase):

    def test_create_reservation(self):
        start_date = datetime.now() + timedelta(days=20)
        end_date = start_date + timedelta(days=30)
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        url = '/user-reservation/'
        user = get_user()
        accommodation =  get_accommodations()
        activity1 = get_activity()
        activity2 = get_activity()

        token = Token.objects.get(user = user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        data = {
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rooms": 2,
            "client_signature": "Marly Emad William",
            "signature_date": "2020-06-23T14:14:46Z",
            "activities": [activity1.id,activity2.id],
            "accommodations": accommodation.id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)



    def test_reservation_inthepast(self):
        start_date = datetime.now() - timedelta(days=20)
        end_date = start_date + timedelta(days=30)
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        url = '/user-reservation/'
        user = get_user()
        accommodation =  get_accommodations()
        activity1 = get_activity()
        activity2 = get_activity()

        token = Token.objects.get(user = user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        data = {
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rooms": 2,
            "client_signature": "Marly Emad William",
            "signature_date": "2020-06-23T14:14:46Z",
            "activities": [activity1.id,activity2.id],
            "accommodations": accommodation.id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data , {'details': "start can't be in the past"})


    #End before start date
    def test_reservation_time(self):
        start_date = datetime.now() + timedelta(days=20)
        end_date = start_date - timedelta(days=10)
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        url = '/user-reservation/'
        user = get_user()
        accommodation =  get_accommodations()
        activity1 = get_activity()
        activity2 = get_activity()

        token = Token.objects.get(user = user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        data = {
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rooms": 2,
            "client_signature": "Marly Emad William",
            "signature_date": "2020-06-23T14:14:46Z",
            "activities": [activity1.id,activity2.id],
            "accommodations": accommodation.id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data , {"details": "start must be before end date"})


class UpdateReservationTests(APITestCase):

    def test_same_user(self):
        reservation = create_reservation()

        token = Token.objects.get(user__username = "test1234")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        start_date = datetime.now() + timedelta(days=20)
        end_date = start_date + timedelta(days=10)
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        accommodation =  get_accommodations()
        activity1 = get_activity()
        activity2 = get_activity()
        url = "/reservation/" + str(reservation.id) + "/"
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rooms": 10,
            "client_signature": "Marly Emad William",
            "signature_date": "2020-06-23T14:14:46Z",
            "activities": [activity1.id,activity2.id],
            "accommodations": accommodation.id
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_different_user(self):
        reservation = create_reservation()

        user = get_user2()
        token = Token.objects.get(user__username = "test2")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        start_date = datetime.now() + timedelta(days=20)
        end_date = start_date + timedelta(days=10)
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        accommodation =  get_accommodations()
        activity1 = get_activity()
        activity2 = get_activity()
        url = "/reservation/" + str(reservation.id) + "/"
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rooms": 10,
            "client_signature": "Marly Emad William",
            "signature_date": "2020-06-23T14:14:46Z",
            "activities": [activity1.id,activity2.id],
            "accommodations": accommodation.id
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data , {'data' : 'You are not allowed to update that reservation'})


    def test_past_startdate(self):
        reservation = create_reservation()

        token = Token.objects.get(user__username = "test1234")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        start_date = datetime.now() - timedelta(days=20)
        end_date = start_date + timedelta(days=10)
        start_date = start_date.strftime("%Y-%m-%d")
        end_date = end_date.strftime("%Y-%m-%d")
        accommodation =  get_accommodations()
        activity1 = get_activity()
        activity2 = get_activity()
        url = "/reservation/" + str(reservation.id) + "/"
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "number_of_rooms": 10,
            "client_signature": "Marly Emad William",
            "signature_date": "2020-06-23T14:14:46Z",
            "activities": [activity1.id,activity2.id],
            "accommodations": accommodation.id
        }

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data , {'details': "start can't be in the past"})


class deleteReservationTests(APITestCase):

    def test_same_user(self):
        reservation = create_reservation()

        token = Token.objects.get(user__username = "test1234")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = "/reservation/" + str(reservation.id) + "/"
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data , {'data' : 'Record deleted'})



    def test_different_user(self):
        reservation = create_reservation()

        user = get_user2()
        token = Token.objects.get(user__username = "test2")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = "/reservation/" + str(reservation.id) + "/"

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data , {'data' : 'You are not allowed to delete that reservation'})


class GetReservationTests(APITestCase):

    def test_get_reservation(self):
        user = get_user()
        token = Token.objects.get(user = user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = '/user-reservation/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)