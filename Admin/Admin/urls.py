from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),  # Changed to django-admin to avoid conflict
    path('', include('adminapp.urls')),  # Include the adminapp URLs
]