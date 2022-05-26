from django.contrib import admin
from .models import *

# Register each DB Model on Admin Site

admin.site.register(Customer)
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(AircraftRow)
admin.site.register(AircraftSeat)
admin.site.register(ScheduledFlight)
admin.site.register(InFlightService)
admin.site.register(FlightReservation)
admin.site.register(ScheduledFlightSeat)
