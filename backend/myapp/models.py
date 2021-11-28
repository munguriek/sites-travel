from django.db import models
from django.db.models.fields.files import ImageField


BUDGET = (
    ('budget', 'budget'),
    ('mid range', 'mid range'),
    ('up market', 'up market'),
)
class Accomadation(models.Model):
    """For both hotel and destination housing"""
    name = models.CharField(max_length=100)
    budget = models.CharField(max_length=100, choices=BUDGET)

    def __str__(self):
        return f"{self.name}"


# PACKAGE_NAME = (
#     ('safari', 'safari'),
#     ('culture', 'culture'),
#     ('holiday', 'holiday'),
#     ('pilgramage', 'pilgramage'),
#     ('kampala special', 'kampala special'),
# )
class PackageCategory(models.Model):
    """Prepopulate into package, eg are safari, culture."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Activity(models.Model):
    """Prepopulate into package, eg culture sAccomadationite vist."""
    package = models.ForeignKey(PackageCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    make = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cars")

    def __str__(self):
        return f"{self.make}"


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="cars")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


DRIVER = (
    ('driver', 'driver'),
    ('self', 'self'),
)
TRIP = (
    ('up country', 'up country'),
    ('town service', 'town service'),
)
class CarHire(models.Model):
    """Prepopulate into package."""
    budget = models.CharField(max_length=100, choices=BUDGET)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    trip = models.CharField(max_length=100, choices=TRIP)
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.car}"


PACKAGE_TYPES = (
    ('group', 'group'),
    ('custom', 'custom'),
)
class Trip(models.Model):
    """Slots for group are read only, for custom is number of editable """
    type = models.CharField(max_length=100, choices=PACKAGE_TYPES, default="group")
    category = models.ForeignKey(PackageCategory, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    image = models.ImageField(upload_to="package")
    slots = models.PositiveIntegerField(default=0)
    start = models.DateField()
    end = models.DateField()
    price = models.PositiveIntegerField(default=0)
    # activities = models.CharField(max_length=200, choices=PACKAGE_TYPES)
    arrival_accomodation = models.ForeignKey(Accomadation, on_delete=models.CASCADE, related_name="arrival_accom")
    trip_accomodation = models.ForeignKey(Accomadation, on_delete=models.CASCADE, related_name="trip_accom")

    class Meta :
       ordering = ['-id']

    def __str__(self):
        return f"{self.type} trip - {self.destination}"


class Flight(models.Model):
    start = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="flights")

    class Meta :
       ordering = ['-id']

    def __str__(self):
        return f"{self.start} - {self.destination}"


TICKET_TYPE = (
    ('one way', 'one way'),
    ('return', 'return'),
)


SERVICE = (
    ('trip', 'trip'),
    ('flight', 'flight'),
    ('car hire', 'car hire'),
)
class Booking(models.Model):
    service = models.CharField(max_length=50, choices=SERVICE, default="trip")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    car_hire = models.ForeignKey(CarHire, on_delete=models.CASCADE, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    flight_type = models.CharField(max_length=30, choices=TICKET_TYPE) # For flight
    departure_date = models.DateField(max_length=100, null=True) # For flight
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    slots = models.PositiveIntegerField(default=0)
    adults = models.PositiveIntegerField(default=0) # For flight
    children = models.PositiveIntegerField(default=0) # For flight
    infants = models.PositiveIntegerField(default=0) # For flight    

    def __str__(self):
        return f"{self.service} by {self.first_name} {self.last_name}"


IMAGE_CATEGORY = (
    ('gallery', 'gallery'),
    ('partner', 'partner'),
)
class Gallery(models.Model):
    picture = models.ImageField(upload_to="gallery")
    category = models.CharField(max_length=50, choices=IMAGE_CATEGORY, default='gallery')
    caption = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.caption}"



