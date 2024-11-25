# Importing necessary modules and functions
from dataclasses import field  # 'field' from dataclasses (though not used in this code)
from statistics import mode  # 'mode' from statistics (though not used in this code)
from rest_framework import serializers  # Importing serializers from Django REST Framework (DRF)
from MyApps.shipments.models import Correspondence, Shipping, Incident  # Importing the models for serialization

# Serializer for the Correspondence model
class CorrespondenceSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Correspondence  # Specifies the model to serialize
        fields = "__all__"  # Includes all fields from the Correspondence model in the serialized output

# Serializer for the Shipping model
class ShippingSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Shipping  # Specifies the model to serialize
        fields = "__all__"  # Includes all fields from the Shipping model in the serialized output

# Serializer for the Incident model
class IncidentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Incident  # Specifies the model to serialize
        fields = "__all__"  # Includes all fields from the Incident model in the serialized output

class ShipmentByBranchSerializer(serializers.Serializer):
    branch_name = serializers.CharField(source='branch__nameB')
    shipment_status = serializers.CharField(source='status')
    total_shipments = serializers.IntegerField()

class ShipmentSerializer(serializers.ModelSerializer):
    correspondence_code = serializers.CharField(source='correspondence.code')
    shipment_status = serializers.CharField(source='status')
    branch_name = serializers.CharField(source='branch.nameB')
    employee_name = serializers.CharField(source='employee.fullname')

    class Meta:
        model = Shipping
        fields = ['id', 'correspondence_code', 'shipment_status', 'branch_name', 'employee_name']