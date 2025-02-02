# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import user_type_required
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser

# def home(request):
#     return render(request, 'accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return render(request, 'accounts/signup_success.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:dashboard')
        messages.error(request, 'Invalid email or password.')
    else:
        form = CustomUserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def dashboard_view(request):
    user_type = request.user.user_type.lower()
    context = {'user': request.user}
    
    templates = {
        'admin': 'accounts/admin_dashboard.html',
        'doctor': 'accounts/doctor_dashboard.html',
        'patient': 'accounts/patient_dashboard.html'
    }
    
    template_name = templates.get(user_type)
    if not template_name:
        messages.error(request, "Invalid user type")
        return redirect('home')
        
    return render(request, template_name, context)
    # if user_type == 'admin':
    #     return render(request, 'accounts/admin_dashboard.html')
    # elif user_type == 'doctor':
    #     return render(request, 'accounts/doctor_dashboard.html')
    # elif user_type == 'patient':
    #     return render(request, 'accounts/doctor_dashboard.html')
    # else:
    #     return render(request, 'accounts/patient_dashboard.html')

@login_required
@user_type_required(['DOCTOR'])
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')

@login_required
@user_type_required(['PATIENT'])
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
@user_type_required(['ADMIN'])
def admin_dashboard(request):
    context = {
        'total_users': CustomUser.objects.count(),
        'total_doctors': CustomUser.objects.filter(user_type='DOCTOR').count(),
        'total_patients': CustomUser.objects.filter(user_type='PATIENT').count(),
    }
    return render(request, 'accounts/admin_dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')
