"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# include package allows you to use the include() function that will link the urls.py file in the app to the main urls.py file
from django.urls import include 

# Settings allows you to access the MEDIA_URL and MEDIA_ROOT variables
from django.conf import settings

# Static provides access to the Django helper function static( ), which allows you to create URLs from local folder name
from django.conf.urls.static import static

# Import view that is setup in the root views.py
from .views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sales.urls')),
    path('books/', include('books.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

# Extend the urlpatterns parameter to include the media information
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
