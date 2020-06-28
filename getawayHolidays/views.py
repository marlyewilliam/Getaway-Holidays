from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from . import models
from . import serializers
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions as per
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin

# Create your views here.

def get_user(request):
    token_value = request.META.get('HTTP_AUTHORIZATION').split()[1]
    token = Token.objects.get(key = token_value)
    user_id = token.user_id
    return user_id

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.ClientSerializer


class UserReservation(APIView, UpdateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (per.IsAuthenticated,)

    def post(self, request):
        if 'start_date' not in request.data and 'end_date' not in request.data:
            return Response({"details": "start and end date must be provided"}, status=status.HTTP_400_BAD_REQUEST)
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        if start_date < datetime.now():
            return Response({"details": "start can't be in the past"}, status=status.HTTP_400_BAD_REQUEST)


        if start_date > end_date:
            return Response({"details": "start must be before end date"}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        user = get_user(request)
        user = User.objects.get(id=user)
        # data['user'] = user
        # return Response({'data' : data})
        serializer = serializers.UserReservationSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            obj.user = user
            obj.save()
            return Response({'data' : serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        user_id = get_user(request)
        reservations = models.Reservations.objects.filter(user__id = user_id)
        serializer = serializers.GetReservationSerializer(reservations, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        

class Reservation(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (per.IsAuthenticated,)
    
    def put(self, request, pk):
        reservation = models.Reservations.objects.get(id=pk)
        user = get_user(request)
        user = User.objects.get(id=user)
        if reservation.user != user:
            return Response({'data' : 'You are not allowed to update that reservation'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'start_date' not in request.data and 'end_date' not in request.data:
            return Response({"details": "start and end date must be provided"}, status=status.HTTP_400_BAD_REQUEST)
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        if start_date < datetime.now():
            return Response({"details": "start can't be in the past"}, status=status.HTTP_400_BAD_REQUEST)


        if start_date > end_date:
            return Response({"details": "start must be before end date"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.UserReservationSerializer(reservation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data' : serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        reservation = models.Reservations.objects.get(id=pk)
        user = get_user(request)
        user = User.objects.get(id=user)
        if reservation.user != user:
            return Response({'data' : 'You are not allowed to delete that reservation'}, status=status.HTTP_400_BAD_REQUEST)
        
        reservation.delete()
        return Response({'data' : 'Record deleted'}, status=status.HTTP_200_OK)





class StaffReservation(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (per.IsAuthenticated,)
    queryset = models.Reservations.objects.all()
    serializer_class = serializers.ReservationSerializer