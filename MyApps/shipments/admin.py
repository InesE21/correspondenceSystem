from django.contrib import admin
from MyApps.shipments.models import *

# Register your models here.

class CorrespondenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Correspondence, CorrespondenceAdmin)

class ShippingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shipping, ShippingAdmin)

class IncidentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Incident, IncidentAdmin)