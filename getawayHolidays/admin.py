from django.contrib import admin

# Register your models here.from .Equipment import *
from .models import *
from .models.Activity import *
from .models.Employee import *


admin.site.register(Equipments)
admin.site.register(EquipmentConditions)
admin.site.register(Suppliers)
admin.site.register(Accommodations)
admin.site.register(Rooms)
admin.site.register(Activities)
admin.site.register(ActivitySchedule)
admin.site.register(Employees)
admin.site.register(OutdoorInstructors)
admin.site.register(Masseuse)
admin.site.register(SwimmingInstructors)
