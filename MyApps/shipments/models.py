from django.db import models
from MyApps.persons.models import *
from MyApps.logistics.models import *
from MyApps.branches.models import *
import random
import string

# Models for managing Correspondence, Shipping, and Incidents in the logistics system.
# Correspondence tracks package details, Shipping tracks their delivery status, and Incident logs issues.

class Correspondence(models.Model):
    """
    Represents a package or document being shipped between two customers. 
    Includes details like tracking code, weight, dimensions, sender, receiver, and the associated service.
    """
    code = models.CharField(max_length=6, unique=True, editable=False, verbose_name="code follow")
    correspondenceType = models.CharField(max_length=30, verbose_name="correspondence type")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="weight")
    dimensions = models.CharField(max_length=50, verbose_name="dimensions")
    shipmentDate = models.DateField(verbose_name="shipment date")
    deliveryDate = models.DateField(verbose_name="delivery date")
    sender = models.ForeignKey(
        Customer, 
        related_name='sent_correspondences', 
        verbose_name="sender", 
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        Customer,  
        related_name='received_correspondences', 
        verbose_name="receiver", 
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="service")

    def generate_tracking_code(self):
        """
        Generate a unique 6-character alphanumeric tracking code.
        """
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=6))

    def save(self, *args, **kwargs):
        """
        Override save method to automatically generate a tracking code if not already set.
        """
        if not self.code:
            self.code = self.generate_tracking_code()
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of Correspondence showing its tracking code.
        """
        return self.code
    
    class Meta:
        verbose_name = "correspondence"
        verbose_name_plural = "correspondences"


class Shipping(models.Model):
    """
    Tracks the status and progress of correspondence shipments.
    Includes details like current status, timestamp, related correspondence, branch, and employee responsible.
    """
    SHIPPING_STATUS_CHOICES = [
        ['AT ORIGIN', 'At origin'],
        ['AT DESTINATION', 'At destination'],
        ['ON THE WAY', 'On the way'],
        ['DELIVERED', 'Delivered'],
    ]

    status = models.CharField(
        max_length=20, 
        choices=SHIPPING_STATUS_CHOICES, 
        help_text="Select shipping status."
    )
    dateTime = models.DateTimeField(verbose_name="date and time")
    correspondence = models.ForeignKey(
        Correspondence, 
        verbose_name="correspondence", 
        on_delete=models.CASCADE
    )
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="branch")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="employee")

    def __str__(self):
        """
        String representation showing shipping status and timestamp.
        """
        return f'{self.status} -> {self.dateTime}'
    
    class Meta:
        verbose_name = "shipping"
        verbose_name_plural = "shippings"


class Incident(models.Model):
    """
    Logs issues or incidents related to correspondence.
    Includes a description, timestamp, resolution status, and associated correspondence.
    """
    description = models.TextField(max_length=250, verbose_name="description")
    incidentDate = models.DateTimeField(verbose_name="incident date")
    RESOLUTION_STATUS_CHOICES = [
        ['REPORTED', 'Reported'],
        ['SCALED', 'Scaled'],
        ['IN RESOLUTION', 'In resolution'],
        ['RESOLVED', 'Resolved'],
        ['CLOSED', 'Closed'],
    ]

    resolutionStatus = models.CharField(
        max_length=20, 
        choices=RESOLUTION_STATUS_CHOICES
    )
    correspondence = models.ForeignKey(
        Correspondence, 
        verbose_name="correspondence", 
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        String representation showing incident description and resolution status.
        """
        return f'{self.description} -> {self.resolutionStatus}'
