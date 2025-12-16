from django.db import models
from django.contrib.auth.models import User
from movie.models import Movie

class BookingTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seats = models.IntegerField()
    bookingDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.seats} seats for {self.movie.title}"