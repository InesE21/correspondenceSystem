from django.contrib import admin
from .models import Transport, Route, Service

# class RouteTransportInline(admin.TabularInline):
#     model = RouteTransport
#     extra = 1  # Cuántas instancias vacías mostrar para añadir

class TransportAdmin(admin.ModelAdmin):
    list_display = ('transportation', 'capacity')
    search_fields = ('transportation',)

class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'stops')
    search_fields = ('origin', 'destination')
    # inlines = (RouteTransportInline,)

# class RouteTransportAdmin(admin.ModelAdmin):
#     list_display = ('route', 'transport')
#     list_filter = ('route', 'transport')

# Registro de modelos en el admin
admin.site.register(Transport, TransportAdmin)
admin.site.register(Route, RouteAdmin)
# admin.site.register(RouteTransport, RouteTransportAdmin)
class ServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)