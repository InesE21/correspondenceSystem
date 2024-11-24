from django.contrib import admin
from MyApps.persons.models import *

class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employee, EmployeeAdmin)