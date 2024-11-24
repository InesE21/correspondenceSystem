from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from MyApps.persons.models import *
from MyApps.persons.serializers import CustomerSerializer, CustomerListSerializer, EmployeeSerializer, EmployeeListSerializer  


# View to handle listing and creating customers
class CustomerList(APIView):

    # Handles GET requests to list all customers
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerListSerializer(customers, many=True)
        return Response({"customers": serializer.data})

    # Handles POST requests to create a new customer
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle detailed operations for a single customer
class CustomerDetail(APIView):

    # Retrieves a customer object by its primary key (pk)
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    # Handles GET requests to retrieve a specific customer's details
    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerListSerializer(customer)
        return Response({"customer": serializer.data})

    # Handles PUT requests to update all fields of a specific customer
    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handles PATCH requests to update partial fields of a specific customer
    def patch(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handles DELETE requests to remove a specific customer
    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# View to handle listing and creating employees
class EmployeeList(APIView):

    # Handles GET requests to list all employees
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeListSerializer(employees, many=True)
        return Response({"employees": serializer.data})

    # Handles POST requests to create a new employee
    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View to handle detailed operations for a single employee
class EmployeeDetail(APIView):

    # Retrieves an employee object by its primary key (pk)
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    # Handles GET requests to retrieve a specific employee's details
    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeListSerializer(employee)
        return Response({"employee": serializer.data})

    # Handles PUT requests to update all fields of a specific employee
    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handles PATCH requests to update partial fields of a specific employee
    def patch(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handles DELETE requests to remove a specific employee
    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
