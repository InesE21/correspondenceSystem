from django.db import models

# Models for managing logistics: Transport, Route, and Service.

class Transport(models.Model):
    """
    Represents the transportation methods available for shipping correspondence.
    Each transport has a type (e.g., Plane, Truck, Motorbike) and a capacity.
    """
    TRANSPORT_TYPE_CHOICES = [
        ['PLANE', 'Plane'],
        ['TRUCK', 'Truck'],
        ['MOTORBIKE', 'Motorbike'],
    ]

    transportation = models.CharField(
        max_length=11, 
        choices=TRANSPORT_TYPE_CHOICES, 
        help_text="Select type transport"
    )
    capacity = models.IntegerField(verbose_name="capacity")

    def __str__(self):
        """
        String representation showing the transport type and its capacity.
        """
        return f'{self.transportation} -> {self.capacity}'

    class Meta:
        verbose_name = "transport"
        verbose_name_plural = "transports"


class Route(models.Model):
    """
    Represents a delivery route with an origin, destination, optional stops, and the associated transport.
    """
    origin = models.CharField(max_length=50, verbose_name="origin")
    destination = models.CharField(max_length=50, verbose_name="destination")
    stops = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        verbose_name="stops"
    )
    transport = models.ForeignKey(
        Transport, 
        on_delete=models.CASCADE, 
        verbose_name='Transport'
    )

    def __str__(self):
        """
        String representation showing the route's origin and destination.
        """
        return f'{self.origin} -> {self.destination}'

    class Meta:
        verbose_name = "route"
        verbose_name_plural = "routes"


class Service(models.Model):
    """
    Represents the type of shipping service offered.
    Each service has a type (e.g., Express, Normal) and an associated cost.
    """
    SERVICE_TYPE_CHOICES = [
        ['EXPRESS', 'Express'],
        ['NORMAL', 'Normal'],
    ]

    transportation = models.CharField(
        max_length=11, 
        choices=SERVICE_TYPE_CHOICES, 
        help_text="Select type transport"
    )
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="cost")

    def __str__(self):
        """
        String representation showing the service type.
        """
        return self.transportation

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"

# Uncomment and use this model if you need to establish many-to-many relationships between routes and transports.
# class RouteTransport(models.Model):
#     """
#     Represents a many-to-many relationship between Route and Transport.
#     Useful if multiple transports can serve a single route and vice versa.
#     """
#     route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name="route")
#     transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name="transport")
