from django.contrib import admin
from django.urls import path, include
from adminapp.views import home_view, custom_admin_dashboard, register_user, api_stats

urlpatterns = [
    path('admin/', custom_admin_dashboard, name='custom_admin_dashboard'),  # Custom admin panel  # Keep Django’s default admin
    path('', include('adminapp.urls')),  # Include the adminapp URLs
    path('register/', register_user, name='register'),
]
