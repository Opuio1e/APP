from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Payment
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import JsonResponse
from .forms import CustomUserForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def api_stats(request):
    # Add sample data if no payments exist
    if Payment.objects.count() == 0:
        return JsonResponse({'values': [12, 19, 3, 5, 15]})
    values = list(Payment.objects.order_by('-timestamp').values_list('amount', flat=True)[:5])
    return JsonResponse({'values': values[::-1]})


def home_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('custom_admin_dashboard')
    return redirect('login')


@login_required
@staff_member_required
def custom_admin_dashboard(request):
    user_count = User.objects.count()
    total_payments = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    recent_users = User.objects.order_by('-date_joined')[:5]

    return render(request, 'appadmin/index.html', {
        'user_count': user_count,
        'total_payments': total_payments,
        'recent_users': recent_users,
    })


def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')