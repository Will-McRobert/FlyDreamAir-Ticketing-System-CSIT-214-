from django.urls import path

from . import views

# Site URL Paths

urlpatterns = [
    path('', views.index, name='index'),
    path('flight-select', views.flight_select, name='flight_select'),
    path('seat-select', views.seat_select, name='seat_select'),
    path('service-select', views.service_select, name='service_select'),
    path('user-payment', views.user_payment, name='user_payment'),
    path('ticket-confirmation', views.ticket_confirmation, name='ticket_confirmation')
]
