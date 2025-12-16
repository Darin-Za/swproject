from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
]
