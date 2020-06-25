from .Equipment import *
from .Accommodation import *
from .Activity import *
from .Employee import *
from .Client import *
from django.db import models


class Reservations(models.Model):
    user = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    reservation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    activities = models.ManyToManyField(Activities, null = True)
    accommodations =  models.ForeignKey(Accommodations, null = False, on_delete = models.CASCADE)
    number_of_rooms = models.IntegerField(default=1, null = False)
    connecting_rooms = models.BooleanField(default=False)
    client_signature = models.CharField(max_length = 255, null = False)
    signature_date = models.DateTimeField(null = False)
    agent_signature =  models.CharField(max_length = 255, null = True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    duration = models.DurationField(null = True)


    def save(self, *args, **kwargs):
        self.duration = self.end_date - self.start_date
        super(Reservations, self).save(*args, **kwargs)

    class Meta:
        app_label = 'getawayHolidays'