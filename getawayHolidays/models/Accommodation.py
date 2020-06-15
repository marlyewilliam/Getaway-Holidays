from django.db import models
from djmoney.models.fields import MoneyField

class Accommodations(models.Model):
    Name = models.CharField(max_length = 255, null = False)
    description = models.TextField(null = False)
    people_per_room = models.IntegerField(default=0, null = False)
    number_of_rooms = models.IntegerField(default=0, null = False)
    price_per_day = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = 'getawayHolidays'


class Rooms(models.Model):
    room_number = models.CharField(max_length = 10, null = False)
    level = models.CharField(max_length = 10, null = False)
    accommodation =  models.ForeignKey(Accommodations, null = False, on_delete = models.CASCADE)
    connected_room = models.OneToOneField('self', null = True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = 'getawayHolidays'
    
