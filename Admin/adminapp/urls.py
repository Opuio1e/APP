from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home_view, custom_admin_dashboard, register_user, api_stats, logout_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', custom_admin_dashboard, name='custom_admin_dashboard'),
    path('register/', register_user, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/stats/', api_stats, name='api_stats'),
]