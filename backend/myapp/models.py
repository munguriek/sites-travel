from django.db import models
from django.db.models.fields.files import ImageField
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
User = get_user_model()

BUDGET = (
    ('budget', 'budget'),
    ('mid range', 'mid range'),
    ('up market', 'up market'),
)
class Accomadation(models.Model):
    """For both hotel and destination housing"""
    name = models.CharField(max_length=100)
    budget = models.CharField(max_length=100, choices=BUDGET)
    available = models.BooleanField(default=True)

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


CAR_CATEGORY = (
    ('executive', 'executive'),
    ('4x4', '4x4'),
    ('safari', 'safari'),
    ('vans', 'vans'),
    ('salon', 'salon'),
    ('buses', 'buses'),
    ('pickups', 'pickups'),
    ('trucks', 'trucks'),
)
class Car(models.Model):
    make = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cars")
    category = models.CharField(max_length=50, choices=CAR_CATEGORY)
    rating = models.FloatField(default=1.0)
    capacity = models.PositiveIntegerField(default=3)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make}"


PERMIT_CLASSES = (
    ('A', 'A - Motorcycles'),
    ('B', 'B - Motorcars and dual-purpose motor vehicles(Passenger vehicles up to 7 people and Goods vehicles up to 3.5 tonnes)'),
    ('CM', 'CM - Motorcars and dual-purpose motor vehicles'),
    ('CH', 'CH - Heavy goods vehicles'),
    ('DL', 'DL - Light omnibuses'),
    ('DM', 'DM - Medium omnibuses'),
    ('DH', 'DH - Heavy omnibuses'),
    ('E', 'E - Combination of vehicles'),
    ('F', 'F - Pedestrian-controlled vehicles'),
    ('G', 'G - Engineering plant vehicle'),
    ('H', 'G - Tractors'),
    ('I', 'G - Boats'),
)
class Driver(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    full_name = models.CharField(max_length=50)
    permit_class = models.CharField(max_length=100, default="DL")
    permit = models.FileField(upload_to="permits")
    photo = models.ImageField(upload_to="cars")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"


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
    available = models.BooleanField(default=True)
    # def depleted_slots:

    class Meta :
       ordering = ['-id']

    def __str__(self):
        return f"{self.type} trip - {self.destination}"


class Flight(models.Model):
    start = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="flights")
    available = models.BooleanField(default=True)

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
DRIVER = (
    ('driver', 'our driver'),
    ('self', 'self'),
)
TRIP = (
    ('up country', 'up country'),
    ('town service', 'town service'),
)
class Booking(models.Model):
    service = models.CharField(max_length=50, choices=SERVICE, default="trip")
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car_booking", null=True) # For car hire
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    flight_type = models.CharField(max_length=30, choices=TICKET_TYPE, default='one way') # For flight
    departure_date = models.DateField(max_length=100, null=True) # For flight
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    country = CountryField(blank_label='select country' )
    telephone = models.CharField(max_length=20)
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    start = models.DateField() # For trips, car hire
    end = models.DateField() # For trips, car hire    
    slots = models.PositiveIntegerField(default=0)
    adults = models.PositiveIntegerField(default=0) # For flight
    children = models.PositiveIntegerField(default=0) # For flight
    infants = models.PositiveIntegerField(default=0) # For flight    
    driven_by = models.CharField(max_length=40, choices=DRIVER, default='driver', null=True) # For car hire
    carhire_trip = models.CharField(max_length=100, choices=TRIP, default="up country") # For car hire
    time_booked = models.DateTimeField(auto_now_add=True)

    class Meta :
       ordering = ['-time_booked']

    def __str__(self):
        return f"{self.full_name} booked {self.service}"


IMAGE_CATEGORY = (
    ('gallery', 'gallery'),
    ('partner', 'partner'),
)
class Gallery(models.Model):
    picture = models.ImageField(upload_to="gallery")
    category = models.CharField(max_length=50, choices=IMAGE_CATEGORY, default='gallery')
    caption = models.CharField(max_length=100, null=True)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.caption}"



