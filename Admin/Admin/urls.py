from django.contrib import admin
from django.urls import path, include
from adminapp.views import register_user, custom_admin_dashboard

urlpatterns = [
    path('admin/', custom_admin_dashboard, name='custom_admin_dashboard'),  # Custom admin panel
    path('', include('adminapp.urls')),  # Include the adminapp URLs
    path('register/', register_user, name='register'),
]