from django import forms
from .models import BookingTicket

class BookingForm(forms.ModelForm):
    seats = forms.IntegerField(min_value=1)

    class Meta:
        model = BookingTicket
        fields = ['seats'] 

