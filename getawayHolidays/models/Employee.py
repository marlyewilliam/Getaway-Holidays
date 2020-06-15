from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length = 255, null = False)
    phone = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 255, unique = True)
    is_supervisor = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        app_label = 'getawayHolidays'


class OutdoorInstructors(models.Model):
    unique_id = models.CharField(max_length = 255, null = False, unique=True)
    employee = models.OneToOneField(Employees, null = False, on_delete=models.CASCADE)
    fields_of_expertise = models.TextField(null = False)

    class Meta:
        app_label = 'getawayHolidays'
        unique_together = (('unique_id', 'employee'),)
        

class Masseuse(models.Model):
    unique_id = models.CharField(max_length = 255, null = False, unique=True)
    employee = models.OneToOneField(Employees, null = False, on_delete=models.CASCADE)
    Qualification_area = models.TextField(null = False)

    class Meta:
        app_label = 'getawayHolidays'
        unique_together = (('unique_id', 'employee'),)
        

class SwimmingInstructors(models.Model):
    unique_id = models.CharField(max_length = 255, null = False, unique=True)
    employee = models.OneToOneField(Employees, null = False, on_delete=models.CASCADE)

    class Meta:
        app_label = 'getawayHolidays'
        unique_together = (('unique_id', 'employee'),)
        







