from django.contrib.auth.models import User
from .models import Payment
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,redirect
from django.db.models import Sum
from django.http import JsonResponse
from .forms import CustomUserForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




def api_stats(request):
    values = list(Payment.objects.order_by('-timestamp').values_list('amount', flat=True)[:5])
    return JsonResponse({'values': values[::-1]})

def home_view(request):
    return HttpResponse("Welcome to the custom Django Admin!")

@staff_member_required
def custom_admin_dashboard(request):
    user_count = User.objects.count()
    total_payments = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    recent_users = User.objects.order_by('-date_joined')[:5]

    return render(request, 'admin/index.html', {
        'user_count': user_count,
        'total_payments': total_payments,
        'recent_users': recent_users,
    })
def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = CustomUserForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def custom_admin_dashboard(request):
    return render(request, 'appadmin/custom_admin_dashboard.html')