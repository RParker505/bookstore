from django.contrib import admin

# Import the class/model
from .models import Salesperson

# Register your models here to see them in Django admin.
admin.site.register(Salesperson)
