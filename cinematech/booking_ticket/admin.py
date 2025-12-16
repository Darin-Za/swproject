from django.contrib import admin
from .models import BookingTicket

class BookingTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_message')

    def get_message(self, obj):
        return str(obj)
    get_message.short_description = 'Message'

admin.site.register(BookingTicket, BookingTicketAdmin)
