from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework import status

from MyApps.logistics.models import Transport, Route, Service
from MyApps.logistics.serializers import TransportSerializer, RouteSerializer, ServiceSerializer

# Views for handling Transport, Route, and Service models.
# These include functions for listing, creating, retrieving, updating, and deleting instances.

@api_view(['GET', 'POST'])
def transport_list(request):
    """
    Handle listing all transport records or creating a new transport entry.
    """
    if request.method == 'GET':
        # Fetch all Transport objects and serialize them into JSON format.
        transports = Transport.objects.all()
        serializer = TransportSerializer(transports, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Deserialize JSON payload to create a new Transport instance.
        serializer = TransportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def transport_detail(request, pk):
    """
    Handle retrieving, updating, or deleting a specific transport record by primary key.
    """
    try:
        # Attempt to fetch the requested Transport object by its primary key.
        transport = Transport.objects.get(pk=pk)
    except Transport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize and return the Transport object.
        serializer = TransportSerializer(transport)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Deserialize and update the existing Transport object.
        serializer = TransportSerializer(transport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the Transport object.
        transport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def route_list(request):
    """
    Handle listing all route records or creating a new route entry.
    """
    if request.method == 'GET':
        # Fetch all Route objects and serialize them.
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Deserialize JSON payload to create a new Route instance.
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def route_detail(request, pk):
    """
    Handle retrieving, updating, or deleting a specific route record by primary key.
    """
    try:
        route = Route.objects.get(pk=pk)
    except Route.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RouteSerializer(route)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RouteSerializer(route, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        route.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def service_list(request):
    """
    Handle listing all service records or creating a new service entry.
    """
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    """
    Handle retrieving, updating, or deleting a specific service record by primary key.
    """
    try:
        service = Service.objects.get(pk=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class RouteTransportList(APIView):
#     def get(self, request, format=None):
#         routeTransports = RouteTransport.objects.all()
#         serializer = RouteTransportSerializer(routeTransports, many=True)
#         return Response({"Routes - Transports": serializer.data})

#     def post(self, request, format=None):
#         serializer = RouteTransportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RouteTransportDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return RouteTransport.objects.get(pk=pk)
#         except RouteTransport.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         routeTransport = self.get_object(pk)
#         serializer = RouteTransportSerializer(routeTransport)
#         return Response({"route - transport": serializer.data})

#     def put(self, request, pk, format=None):
#         routeTransport = self.get_object(pk)
#         serializer = RouteTransportSerializer(routeTransport, data=request.data)  
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk, format=None):
#         routeTransport = self.get_object(pk)
#         serializer = RouteTransportSerializer(routeTransport, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)