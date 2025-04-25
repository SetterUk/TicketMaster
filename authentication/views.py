from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('booking:home')
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        # Manual form handling as per requirements
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation
        if password1 != password2:
            messages.error(request, "Passwords don't match")
            return render(request, 'authentication/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'authentication/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'authentication/register.html')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        # Log in the user
        login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('booking:home')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('booking:home')
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            redirect_url = request.GET.get('next', 'booking:home')
            return redirect(redirect_url)
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'authentication/login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('booking:home')
