from django.shortcuts import render , redirect
from movie.models import Movie
from django.views import View
from django.contrib.auth import logout


def welcome(request):
    movies = Movie.objects.all()
    return render(request, 'welcome.html', {'movies': movies})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

# Logout

class LogoutView(View):

    def post(self, request):
        logout(request)
        return redirect("login")