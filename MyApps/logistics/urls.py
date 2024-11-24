"""
API Endpoints for Logistics Views

This file defines the URL patterns for the logistics application, mapping them to their corresponding view functions. 
These endpoints provide CRUD operations for Transport, Service, and Route models.
"""

from django.urls import path
from MyApps.logistics.views import (
    transport_list,
    transport_detail,
    service_list,
    service_detail,
    route_list,
    route_detail
)

urlpatterns = [
    # URL for retrieving the list of all transports or creating a new transport
    path('transport/', transport_list, name='transport_list'),
    # URL for retrieving, updating, or deleting a specific transport by ID
    path('transport/<int:pk>/', transport_detail, name='transport_detail'),
    
    # URL for retrieving the list of all services or creating a new service
    path('service/', service_list, name='service_list'),
    # URL for retrieving, updating, or deleting a specific service by ID
    path('service/<int:pk>/', service_detail, name='service_detail'),
    
    # URL for retrieving the list of all routes or creating a new route
    path('route/', route_list, name='route_list'),
    # URL for retrieving, updating, or deleting a specific route by ID
    path('route/<int:pk>/', route_detail, name='route_detail'),
]
