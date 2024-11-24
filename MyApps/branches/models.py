# This model represents a branch within the correspondence system.
# Each branch has a name and a location, providing basic details about its presence.

from django.db import models

class Branch(models.Model):
    # Name of the branch, limited to 100 characters.
    nameB = models.CharField(max_length=100, verbose_name="branch name")
    
    # Location of the branch, stored as a text field with a maximum length of 255 characters.
    location = models.CharField(max_length=255, verbose_name="branch location")

    def __str__(self):
        # String representation of the branch, returning its name for easy identification in the admin panel and logs.
        return self.nameB

    class Meta:
        # Metadata specifying the singular and plural names for the model, 
        # used in Django admin and other human-readable contexts.
        verbose_name = "branch"
        verbose_name_plural = "branches"