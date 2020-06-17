from .Equipment import *
from .Accommodation import *
from .Activity import *
from .Employee import *
from .Client import *
from django.db import models


class Reservations(models.Model):
    client_id = models.ForeignKey(ClientsProfile, null = False, on_delete = models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    activities = models.ForeignKey(Activities, null = True, on_delete = models.SET_NULL)
    accommodations =  models.ForeignKey(Accommodations, null = False, on_delete = models.CASCADE)
    number_of_rooms = models.IntegerField(default=1, null = False)
    connecting_rooms = models.BooleanField(default=False)
    client_signature = models.CharField(max_length = 255, null = False)
    signature_date = models.DateTimeField(null = False)
    agent_signature =  models.CharField(max_length = 255, null = True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def duration(self):
        delta = end_date - start_date
        return delta.days

    class Meta:
        app_label = 'getawayHolidays'