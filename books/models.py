from django.db import models
from django.shortcuts import reverse

# Create your models here.

genre_choices= (
('classic', 'Classic'), 
('romantic', 'Romantic'), 
('comic', 'Comic'), 
('fantasy', 'Fantasy'), 
('horror', 'Horror'), 
('educational', 'Educational'),
)

book_type_choices=(
('hardcover','Hard cover'),
('ebook', 'E-Book'),
('audiobook', 'Audiobook')
)

# Define class (table) and inherit from models.Model for basic functionality and attributes
class Book(models.Model):

    # Define attributes/columns in the table
    name=models.CharField(max_length=120)
    author_name=models.CharField(max_length=120)
    price = models.FloatField(help_text='in US dollars $')
    genre = models.CharField(max_length=12, choices=genre_choices, default='classic')
    book_type = models.CharField(max_length=12, choices=book_type_choices, default='hardcover')
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')
    
    # Define string representation and the parameter you want to use to refer to the customer
    def __str__(self):
        return str(self.name)

    # Take primary key as an argument and generate a URL
    def get_absolute_url(self):
       return reverse ('books:detail', kwargs={'pk': self.pk})