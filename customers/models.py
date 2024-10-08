from django.db import models

# Create your models here.

# Define class (table) and inherit from models.Model for basic functionality and attributes
class Customer(models.Model):

    # Define attributes/columns in the table
    name = models.CharField(max_length=120)
    notes = models.TextField()
    pic = models.ImageField(upload_to='customers', default='no_picture.png')

    # Define string representation and the parameter you want to use to refer to the customer
    def __str__(self):
        return str(self.name) 