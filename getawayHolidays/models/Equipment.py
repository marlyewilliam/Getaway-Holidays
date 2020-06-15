from django.db import models

class Equipments(models.Model):
    name = models.CharField(max_length = 255, null = False)
    number = models.IntegerField(default=0, null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        app_label = 'getawayHolidays'




class EquipmentConditions(models.Model):
    equipment = models.ForeignKey(Equipments, null = True, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    condition = models.TextField(null = True, blank = True)
    report = models.FileField(upload_to = 'brands/', null = True, blank = True)

    class Meta:
        app_label = 'getawayHolidays'


class Suppliers(models.Model):
    business_name = models.CharField(max_length = 255, null = False)
    contact_person_name = models.CharField(max_length = 255, null = False)
    contact_person_position = models.CharField(max_length = 255, null = False)
    contact_number = models.CharField(max_length = 255, null = False)
    biller_code = models.CharField(max_length = 255)
    equipment = models.ManyToManyField(Equipments, null = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        app_label = 'getawayHolidays'


