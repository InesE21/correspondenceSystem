# URL configuration for the branches app.
# This module defines routes to handle requests for branch-related views.

from django.urls import path
from MyApps.branches.views import BranchList, BranchDetail

# Namespace for the branches app to organize URLs and avoid conflicts.
app_name = "branches"

urlpatterns = [
    # Route for listing all branches or creating a new branch.
    path('', BranchList.as_view()),

    # Route for retrieving, updating, or deleting a specific branch by its primary key.
    path('<int:pk>', BranchDetail.as_view()),
]