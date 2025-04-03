from django.urls import path
from .views import home_view, custom_admin_dashboard, register_user, api_stats

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/dashboard/', custom_admin_dashboard, name='custom_admin_dashboard'),  # Custom admin panel
    path('register/', register_user, name='register'),
    path('api/stats/', api_stats, name='api_stats'),
]
