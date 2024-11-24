# This module provides API views for managing branches.
# It includes list and detail views with support for CRUD operations (Create, Read, Update, Delete).

from django.shortcuts import render
from django.http import Http404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from MyApps.branches.models import Branch
from MyApps.branches.serializers import BranchListSerializer, BranchSerializer 

class BranchList(APIView):
    """
    API view to retrieve a list of branches or create a new branch.
    """

    def get(self, request, format=None):
        # Retrieve all branch objects from the database.
        branches = Branch.objects.all()
        # Serialize the branch objects into JSON format.
        serializer = BranchListSerializer(branches, many=True)
        # Return the serialized branch data in the response.
        return Response({"branches": serializer.data})

    def post(self, request, format=None):
        # Deserialize incoming branch data and validate it.
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            # Save the valid data as a new branch object.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return errors if the data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchDetail(APIView):
    """
    API view to retrieve, update, or delete a specific branch by its primary key (pk).
    """

    def get_object(self, pk):
        # Helper function to retrieve a branch object by its primary key.
        try:
            return Branch.objects.get(pk=pk)
        except Branch.DoesNotExist:
            # Raise a 404 error if the branch does not exist.
            raise Http404

    def get(self, request, pk, format=None):
        # Retrieve a single branch object using the helper function.
        branch = self.get_object(pk)
        # Serialize the branch object into JSON format.
        serializer = BranchListSerializer(branch)
        # Return the serialized branch data in the response.
        return Response({"branch": serializer.data})

    def put(self, request, pk, format=None):
        # Fully update a branch object with the provided data.
        branch = self.get_object(pk)
        serializer = BranchSerializer(branch, data=request.data)  
        if serializer.is_valid():
            # Save the updates if the data is valid.
            serializer.save()
            return Response(serializer.data)
        # Return errors if the data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        # Partially update a branch object with the provided data.
        branch = self.get_object(pk)
        serializer = BranchSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updates if the data is valid.
            serializer.save()
            return Response(serializer.data)
        # Return errors if the data is invalid.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # Delete the specified branch object from the database.
        branch = self.get_object(pk)
        branch.delete()
        # Return a 204 No Content response upon successful deletion.
        return Response(status=status.HTTP_204_NO_CONTENT)
