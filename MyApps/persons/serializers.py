from dataclasses import field
from statistics import mode

from rest_framework import serializers
from MyApps.persons.models import *

# Serializer for the Customer model
# This serializer is used for detailed CRUD operations on the Customer model
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"  # Includes all fields of the Customer model

# Serializer for listing customers
# Provides a simplified representation of Customer objects, suitable for list views
class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"  # Includes all fields of the Customer model

# Serializer for the Employee model
# This serializer is used for detailed CRUD operations on the Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"  # Includes all fields of the Employee model

# Serializer for listing employees
# Provides a simplified representation of Employee objects, suitable for list views
class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"  # Includes all fields of the Employee model
