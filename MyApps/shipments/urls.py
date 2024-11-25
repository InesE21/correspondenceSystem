from django.urls import path
from MyApps.shipments.views import (
    get_pending_shipments,
    shipments_by_branch_and_status,
    shipping_list,
    shipping_detail,
    correspondence_list,
    correspondence_detail,
    incident_list,
    incident_detail,
)

# URL patterns for shipment-related endpoints
urlpatterns = [
    # Endpoint for listing all shippings or creating a new shipping
    path('shipping/', shipping_list),
    # Endpoint for retrieving, updating, or deleting a specific shipping by its primary key (pk)
    path('shipping/<int:pk>/', shipping_detail),
    
    # Endpoint for listing all correspondences or creating a new correspondence
    path('correspondence/', correspondence_list),
    # Endpoint for retrieving, updating, or deleting a specific correspondence by its primary key (pk)
    path('correspondence/<int:pk>/', correspondence_detail),
    
    # Endpoint for listing all incidents or creating a new incident
    path('incident/', incident_list),
    # Endpoint for retrieving, updating, or deleting a specific incident by its primary key (pk)
    path('incident/<int:pk>/', incident_detail),

    path('shipping/by-branch-status/', shipments_by_branch_and_status),

    path('shipping/pending/<int:dni>/', get_pending_shipments),
]
