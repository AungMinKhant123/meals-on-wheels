from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def login_view(request):
    return render(request, 'administration/login.html')

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser, login_url='administration:admin_login')
def dashboard_view(request):
    return render(request, 'administration/dashboard.html')

def login_filled_view(request):

    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add authentication logic as needed

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('administration:admin_dashboard')
        else:
            # Invalid login
            return render(request, 'administration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'administration/login.html')

def logout_view(request):
    logout(request)
    return redirect('administration:admin_login')