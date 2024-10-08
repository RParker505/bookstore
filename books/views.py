from django.shortcuts import render         # imported by default
from django.views.generic import ListView, DetailView   # to display lists and details
from .models import Book                    # to access Book model
# To protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# create class-based protected views as custom logic isn't needed and generic functionality is good enough
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/main.html'

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'