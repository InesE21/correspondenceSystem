from django.db import models
from MyApps.branches.models import Branch
from MyApps.logistics.models import Route


# Model to represent customers
class Customer(models.Model):
    dni = models.IntegerField(unique=True, verbose_name='dni')  # Unique identifier for the customer
    fullname = models.CharField(max_length=50, verbose_name='fullname')  # Customer's full name
    address = models.CharField(max_length=50, verbose_name='address')  # Customer's address
    phoneNumber = models.CharField(max_length=10, unique=True, verbose_name='phone number')  # Unique phone number
    mail = models.EmailField(unique=True, verbose_name='mail')  # Unique email address

    # Customer type choices
    CUSTOMER_TYPE_CHOICES = [
        ['NORMAL', 'Normal'],
        ['PREMIUM', 'Premium'],
    ]

    # Field to store the type of customer (e.g., Normal or Premium)
    customer_type = models.CharField(max_length=7, choices=CUSTOMER_TYPE_CHOICES, help_text="Select Customer Type")

    # String representation of a customer
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "customer"  # Singular name for the model in the admin interface
        verbose_name_plural = "customers"  # Plural name for the model in the admin interface


# Model to represent employees
class Employee(models.Model):
    fullname = models.CharField(max_length=50, verbose_name='fullname')  # Employee's full name

    # Employee position choices
    POSITION_EMPLOYEE_CHOICES = [
        ['MANAGER', 'Manager'],
        ['ADVISOR', 'Advisor'],
        ['DISTRIBUTOR', 'Distributor'],
        ['SUPERVISOR', 'Supervisor'],
    ]

    # Field to store the employee's position
    position = models.CharField(max_length=11, choices=POSITION_EMPLOYEE_CHOICES, help_text="Select Position Employee")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name='Branch')  # Related branch
    assignedRoute = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Assigned Route'
    )  # Assigned route (optional, depends on position)

    def clean(self):
        """
        Custom validation logic for the Employee model.
        Ensures 'assignedRoute' is assigned only for DISTRIBUTOR position and not others.
        """
        from django.core.exceptions import ValidationError

        if self.position == 'DISTRIBUTOR' and not self.assignedRoute:
            raise ValidationError({'assignedRoute': "The assigned route is mandatory for distributors."})
        elif self.position != 'DISTRIBUTOR' and self.assignedRoute:
            raise ValidationError({'assignedRoute': "The route must only be assigned to distributors."})

    # String representation of an employee
    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "employee"  # Singular name for the model in the admin interface
        verbose_name_plural = "employees"  # Plural name for the model in the admin interface
