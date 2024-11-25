from django.urls import path
from MyApps.persons.views import CustomerList, CustomerDetail, EmployeeList, EmployeeDetail, premium_customers_activity, unresolved_incidents_by_customer

# URL patterns for the `persons` app
urlpatterns = [
    # Endpoint for retrieving and creating customers
    path('customer/', CustomerList.as_view(), name='customer_list'),
    
    # Endpoint for retrieving, updating, and deleting a specific customer by primary key
    path('customer/<int:pk>', CustomerDetail.as_view(), name='customer_detail'),
    
    # Endpoint for retrieving and creating employees
    path('employee/', EmployeeList.as_view(), name='employee_list'),
    
    # Endpoint for retrieving, updating, and deleting a specific employee by primary key
    path('employee/<int:pk>', EmployeeDetail.as_view(), name='employee_detail'),

    path('customer/premium-customers-activity/', premium_customers_activity, name='premium-customers'),

    path('customer/unresolved-incidents/<int:dni>/', unresolved_incidents_by_customer, name='unresolved-incidents'),
]
