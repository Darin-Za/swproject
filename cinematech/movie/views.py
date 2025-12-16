from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Movie


# List all movies
class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie/movies_list.html', {'movies': movies})
    
#############################################

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})















