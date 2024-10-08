# path package supports creating paths from the URL to the view
from django.urls import path
# Import the view
from .views import BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
    # Since BookListView and BookDetailView are CBVs, you must call as_view(), a method of ListView that returns a callable view that takes a request and returns a response
    # When books/list is visited, BookListView is loaded
    path('list/', BookListView.as_view(), name='list'),
    path('list/<pk>', BookDetailView.as_view(), name='detail'),
]