from django.db import models
from djmoney.models.fields import MoneyField



class Activities(models.Model):
    Name = models.CharField(max_length = 255, null = False)
    description = models.TextField(null = True)
    activity_type = models.CharField(max_length=24, null = False, choices=(
        (0, 'Indoor'),
        (1, 'Outdoor')))
    risk_level = models.CharField(max_length=24, null = False, choices=(
        (0, 'Low'),
        (1, 'Medium'),
        (1, 'High')))
    duration = models.DurationField()
    price_per_duration =  MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    location = models.CharField(max_length = 255, null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = 'getawayHolidays'

class ActivitySchedule(models.Model):
    activity = models.ForeignKey(Activities, null = False, on_delete = models.CASCADE)
    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField()
    seats_available = models.IntegerField(default=0, null = False)
    supervisor = models.BooleanField(default=False)

    class Meta:
        app_label = 'getawayHolidays'