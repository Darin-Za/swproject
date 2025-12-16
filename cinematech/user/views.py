from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from booking_ticket.models import BookingTicket

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "user/register.html", {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")
        return render(request, "user/register.html", {'form': form})

#Login

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "user/login.html", {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
        return render(request, "user/login.html", {'form': form})



# Profile

class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        bookings = BookingTicket.objects.filter(user=request.user)
        return render(request, "user/profile.html", {"user": request.user, "bookings": bookings})


