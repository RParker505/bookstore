# path package supports creating paths from the URL to the view
from django.urls import path
# Import the view
from .views import home, records

app_name = 'sales'

urlpatterns = [
   path('', home), # when homepage is visited, home view is loaded
   path('sales/', records),
]