from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.logistics.models import Transport, Route, Service

# Serializer for the Transport model
class TransportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transport model. 
    Converts Transport model instances to and from JSON format.
    """
    class Meta:
        model = Transport  # Associated model
        fields = "__all__"  # Include all fields from the model

# Serializer for the Route model
class RouteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Route model.
    Handles data conversion between JSON and Route model instances.
    """
    class Meta:
        model = Route  # Associated model
        fields = "__all__"  # Include all fields from the model

# Serializer for the Service model
class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for the Service model.
    Facilitates data conversion for Service model instances.
    """
    class Meta:
        model = Service  # Associated model
        fields = "__all__"  # Include all fields from the model

class TransportCapacitySerializer(serializers.Serializer):
    transport_type = serializers.CharField(source='transportation')
    total_capacity = serializers.IntegerField()

# Serializer for the RouteTransport model (currently commented in the data model)
# class RouteTransportSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the RouteTransport model.
#     Used for managing data related to the relationship between routes and transports.
#     """
#     class Meta:
#         model = RouteTransport  # Associated model
#         fields = "__all__"  # Include all fields from the model
