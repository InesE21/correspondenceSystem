# Import necessary modules
from django.shortcuts import render  # (Not used in this code but useful for rendering templates if needed)
from django.http import Http404  # For handling "Not Found" exceptions (not used directly in this code)
from rest_framework.response import Response  # For sending structured API responses
from rest_framework.decorators import api_view  # To define function-based API views
from rest_framework import status  # Provides standard HTTP response status codes
from MyApps.shipments.models import Correspondence, Shipping, Incident  # Importing models for database interaction
from MyApps.shipments.serializers import CorrespondenceSerializer, ShippingSerializer, IncidentSerializer  # Importing serializers

# Function-based API view for Correspondence list operations
@api_view(['GET', 'POST'])
def correspondence_list(request):
    """
    Handles listing all Correspondence entries or creating a new one.
    """
    if request.method == 'GET':  # Handle GET requests to list all correspondence
        correspondence = Correspondence.objects.all()  # Retrieve all correspondence records
        serializer = CorrespondenceSerializer(correspondence, many=True)  # Serialize multiple records
        return Response(serializer.data)  # Return serialized data as a response

    elif request.method == 'POST':  # Handle POST requests to create a new correspondence
        serializer = CorrespondenceSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new correspondence record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the created data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors


# Function-based API view for Correspondence detail operations
@api_view(['GET', 'PUT', 'DELETE'])
def correspondence_detail(request, pk):
    """
    Handles retrieving, updating, or deleting a specific Correspondence entry.
    """
    try:
        correspondence = Correspondence.objects.get(pk=pk)  # Try to retrieve the correspondence by primary key
    except Correspondence.DoesNotExist:  # Handle the case where it does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Retrieve a specific correspondence
        serializer = CorrespondenceSerializer(correspondence)  # Serialize the correspondence instance
        return Response(serializer.data)  # Return serialized data

    elif request.method == 'PUT':  # Update an existing correspondence
        serializer = CorrespondenceSerializer(correspondence, data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the updated correspondence record
            return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

    elif request.method == 'DELETE':  # Delete a specific correspondence
        correspondence.delete()  # Remove the record from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a "No Content" response


# Function-based API view for Shipping list operations
@api_view(['GET', 'POST'])
def shipping_list(request):
    """
    Handles listing all Shipping entries or creating a new one.
    """
    if request.method == 'GET':  # Handle GET requests to list all shipping entries
        shipping = Shipping.objects.all()  # Retrieve all shipping records
        serializer = ShippingSerializer(shipping, many=True)  # Serialize multiple records
        return Response(serializer.data)  # Return serialized data as a response

    elif request.method == 'POST':  # Handle POST requests to create a new shipping entry
        serializer = ShippingSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new shipping record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the created data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors


# Function-based API view for Shipping detail operations
@api_view(['GET', 'PUT', 'DELETE'])
def shipping_detail(request, pk):
    """
    Handles retrieving, updating, or deleting a specific Shipping entry.
    """
    try:
        shipping = Shipping.objects.get(pk=pk)  # Try to retrieve the shipping entry by primary key
    except Shipping.DoesNotExist:  # Handle the case where it does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Retrieve a specific shipping entry
        serializer = ShippingSerializer(shipping)  # Serialize the shipping instance
        return Response(serializer.data)  # Return serialized data

    elif request.method == 'PUT':  # Update an existing shipping entry
        serializer = ShippingSerializer(shipping, data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the updated shipping record
            return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

    elif request.method == 'DELETE':  # Delete a specific shipping entry
        shipping.delete()  # Remove the record from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a "No Content" response


# Function-based API view for Incident list operations
@api_view(['GET', 'POST'])
def incident_list(request):
    """
    Handles listing all Incident entries or creating a new one.
    """
    if request.method == 'GET':  # Handle GET requests to list all incidents
        incident = Incident.objects.all()  # Retrieve all incident records
        serializer = IncidentSerializer(incident, many=True)  # Serialize multiple records
        return Response(serializer.data)  # Return serialized data as a response

    elif request.method == 'POST':  # Handle POST requests to create a new incident
        serializer = IncidentSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new incident record to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with the created data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors


# Function-based API view for Incident detail operations
@api_view(['GET', 'PUT', 'DELETE'])
def incident_detail(request, pk):
    """
    Handles retrieving, updating, or deleting a specific Incident entry.
    """
    try:
        incident = Incident.objects.get(pk=pk)  # Try to retrieve the incident by primary key
    except Incident.DoesNotExist:  # Handle the case where it does not exist
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # Retrieve a specific incident
        serializer = IncidentSerializer(incident)  # Serialize the incident instance
        return Response(serializer.data)  # Return serialized data

    elif request.method == 'PUT':  # Update an existing incident
        serializer = IncidentSerializer(incident, data=request.data)  # Deserialize incoming data
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the updated incident record
            return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors

    elif request.method == 'DELETE':  # Delete a specific incident
        incident.delete()  # Remove the record from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return a "No Content" response
