from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BookingTicket
from .forms import BookingForm
from movie.models import Movie
from django.contrib.auth import get_user_model
User = get_user_model()

class BookingCreateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        form = BookingForm()
        movie=get_object_or_404(Movie, pk=pk)
        return render(request, 'booking_ticket/booking.html', {'form': form, 'movie': movie})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        seats = request.POST.get('seats')

        try:
            seats = int(seats)
            if seats < 1:
                raise ValueError
        except (TypeError, ValueError):
            form = BookingForm()
            return render(request, 'booking_ticket/booking.html', {'form': form, 'movie': movie, 'error': 'Please enter a valid number of seats.'})

        booking = BookingTicket.objects.create(
            user=request.user,
            movie=movie,
            seats=seats
        )
        return render(request, 'booking_ticket/booking.html', {
            'form': BookingForm(),
            'movie': movie,
            'booking_id': booking.id,
            'booking_total': (booking.seats * 30),
        })

class BookingDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        booking = get_object_or_404(BookingTicket, pk=pk, user=request.user)
        booking.delete()
        return redirect('profile') 

class BookingListView(LoginRequiredMixin, View):
    def get(self, request):
        bookings = BookingTicket.objects.filter(user=request.user)
        return render(request, "user/profile.html", {"user": request.user, "bookings": bookings})

