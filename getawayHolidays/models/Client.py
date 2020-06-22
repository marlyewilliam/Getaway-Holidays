from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token



class HealthConditions(models.Model):
    name = models.CharField(max_length = 255, null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        app_label = 'getawayHolidays'


class ClientsProfile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length = 255, null = False)
    state = models.CharField(max_length = 255, null = False)
    postcode = models.CharField(max_length = 10, null = True, blank=True)
    contact_number = models.CharField(max_length = 20, null = False)
    occupation = models.CharField(max_length = 255, null = True, blank=True)
    marital_status = models.CharField(max_length=24, null = False, choices=(
        ('Single', 'Single'),
        ('Married', 'Married')))
    spouse = models.CharField(max_length = 255, null=True, blank=True)
    anniversary = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=24, null = False, choices=(
        ('Male', 'Male'),
        ('Female', 'Female')))
    city = models.CharField(max_length = 255, null = False)
    birthday = models.DateField(null=False)
    health_conditions = models.ManyToManyField(HealthConditions, null = True, blank=True)
    client_signature = models.CharField(max_length = 255, null = False)
    signature_date = models.DateTimeField(null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)


    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    class Meta:
        app_label = 'getawayHolidays'

