from django.db import models

# DB Model Definitions


class Customer(models.Model):
    class Meta:
        db_table = "customer"

    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'Customer: #{self.id} {self.email}'


class Airport(models.Model):
    class Meta:
        db_table = "airport"

    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return f'Airport: {self.name}, {self.city}'


class Aircraft(models.Model):
    class Meta:
        db_table = "aircraft"

    code = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=50)
    seat_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'Aircraft: {self.name}'


class AircraftRow(models.Model):
    class Meta:
        db_table = "aircraft_row"
        unique_together = (('aircraft', 'code'),)

    code = models.PositiveIntegerField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    seat_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.aircraft.name} Row {self.code}'


class AircraftSeat(models.Model):
    class Meta:
        db_table = "aircraft_seat"
        unique_together = (('aircraft', 'row', 'code'),)

    code = models.CharField(max_length=1)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    row = models.ForeignKey(AircraftRow, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.aircraft.name} Seat {self.row.id}{self.code}'


class ScheduledFlight(models.Model):
    class Meta:
        db_table = "scheduled_flight"

    FLIGHT_CLASSES = (
        ('E', 'Economy'),
        ('PE', 'Premium Economy'),
        ('B', 'Business'),
        ('F', 'First')
    )

    flight_class = models.CharField(max_length=2, choices=FLIGHT_CLASSES)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    origin_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='origin_airport')
    destination_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_airport')
    departure_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    total_seats_remaining = models.PositiveIntegerField()

    def __str__(self):
        return f'Flight: {self.flight_class} class {self.aircraft.code} from {self.origin_airport.name} to ' \
               f'{self.destination_airport.name} @{self.departure_date_time}'


class ScheduledFlightSeat(models.Model):
    class Meta:
        db_table = "scheduled_flight_seat"
        unique_together = (('aircraft_seat', 'scheduled_flight'),)

    aircraft_seat = models.ForeignKey(AircraftSeat, on_delete=models.CASCADE)
    scheduled_flight = models.ForeignKey(ScheduledFlight, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f'Seat: {self.aircraft_seat.row}{self.aircraft_seat.code} for flight {self.scheduled_flight}'


class InFlightService(models.Model):
    class Meta:
        db_table = "in_flight_service"

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'In Flight Service: {self.name}'


class FlightReservation(models.Model):
    class Meta:
        db_table = "flight_reservation"
        unique_together = (('flight', 'flight_seat'),)

    flight = models.ForeignKey(ScheduledFlight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seat_row = models.ForeignKey(AircraftRow, on_delete=models.CASCADE)
    flight_seat = models.ForeignKey(ScheduledFlightSeat, on_delete=models.CASCADE)

    def __str__(self):
        return f'Flight Reservation: customer #{self.customer.id} ({self.customer.email}) for {self.flight}'
