# Serializers for the branches app.
# These classes define how branch model instances are converted to and from JSON for API interactions.

from rest_framework import serializers
from MyApps.branches.models import Branch

class BranchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Branch model, used for full CRUD operations.
    Includes all fields of the Branch model.
    """
    class Meta:
        model = Branch
        fields = "__all__"  # Automatically include all model fields.

class BranchListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing Branch objects.
    Includes all fields of the Branch model, similar to BranchSerializer.
    This separation allows future customization for list-specific behavior if needed.
    """
    class Meta:
        model = Branch
        fields = "__all__"
