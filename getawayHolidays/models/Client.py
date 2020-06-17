from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class HealthConditions(models.Model):
    name = models.CharField(max_length = 255, null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = 'getawayHolidays'


class ClientsProfile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    address = models.CharField(max_length = 255, null = False)
    state = models.CharField(max_length = 255, null = False)
    postcode = models.CharField(max_length = 10, null = True)
    contact_number = models.CharField(max_length = 20, null = False)
    occupation = models.CharField(max_length = 255, null = True)
    marital_status = models.CharField(max_length=24, null = False, choices=(
        (0, 'single'),
        (1, 'married')))
    spouse = models.CharField(max_length = 255, null = True)
    anniversary = models.DateTimeField()
    gender = models.CharField(max_length=24, null = False, choices=(
        (0, 'Male'),
        (1, 'Female')))
    city = models.CharField(max_length = 255, null = False)
    birthday = models.DateField(null=False)
    health_conditions = models.ManyToManyField(HealthConditions, null = True)
    client_signature = models.CharField(max_length = 255, null = False)
    signature_date = models.DateTimeField(null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        app_label = 'getawayHolidays'

