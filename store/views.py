from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Site View Definitions


def index(request):
    context = {
    }

    return render(request, 'index.html', context)


def flight_select(request):
    if request.method == 'POST':
        origin_airport = request.POST['origin-airport']
        destination_airport = request.POST['destination-airport']

    origin_airport = Airport.objects.get(city=origin_airport)
    destination_airport = Airport.objects.get(city=destination_airport)
    available_flights = ScheduledFlight.objects.all().order_by('departure_date_time')

    context = {
        'available_flights': available_flights
    }
    
    return render(request, 'flight-select.html', context)


@csrf_exempt
def seat_select(request):
    flight_seats = ScheduledFlightSeat.objects.filter(scheduled_flight_id = request.POST['flight-id'])

    context = {
        'scheduled_flight_seats': flight_seats
    }

    return render(request, 'seat-select.html', context)


@csrf_exempt
def service_select(request):
    selected_seat = ScheduledFlightSeat.objects.get(id=request.POST['seat-id'])

    additional_services = InFlightService.objects.all()

    context = {
        'selected_seat': selected_seat,
        'additional_services': additional_services
    }

    return render(request, 'service-select.html', context)


@csrf_exempt
def user_payment(request):
    selected_seat = ScheduledFlightSeat.objects.get(id=request.POST['seat-id'])

    context = {
        'selected_seat': selected_seat,
    }

    return render(request, 'user-payment.html', context)


@csrf_exempt
def ticket_confirmation(request):
    selected_seat = ScheduledFlightSeat.objects.get(id=request.POST.get('seat-id'))
    passenger_details = {
        'passenger_name': request.POST.get('passenger-name'),
        'passenger_email': request.POST.get('passenger-email'),
        'passenger_phone': request.POST.get('passenger-phone'),
        'passenger_credit_card': request.POST.get('card-number')
    }

    context = {
        'selected_flight': selected_seat.scheduled_flight,
        'selected_seat': selected_seat,
        'passenger': passenger_details
    }

    return render(request, 'ticket-confirmation.html', context)
