from django.urls import path
from .views import*

urlpatterns = [
    path('', BookingListView.as_view(), name='booking-list'),
    path('create/<int:pk>/',BookingCreateView.as_view(), name='booking_create'),
    path('<int:pk>/delete/', BookingDeleteView.as_view(), name='booking-delete'),
]
