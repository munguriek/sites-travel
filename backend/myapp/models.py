from django.db import models


BUDGET = (
    ('budget', 'budget'),
    ('mid range', 'mid range'),
    ('up market', 'up market'),
)
class Accomadation(models.Model):
    """For both hotel and destination housing"""
    name = models.CharField(max_length=100)
    budget = models.CharField(max_length=100, choices=BUDGET)


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

class Activity(models.Model):
    """Prepopulate into package, eg culture site vist."""
    package = models.ForeignKey(PackageCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


DRIVER = (
    ('driver', 'driver'),
    ('self', 'self'),
)
TRIP = (
    ('Up Country', 'Up Country'),
    ('Town Service', 'Town Service'),
)
class Transport(models.Model):
    """Prepopulate into package."""
    budget = models.CharField(max_length=100, choices=BUDGET)
    car = models.CharField(max_length=100)
    driver = models.CharField(max_length=100, choices=DRIVER)
    budget = models.CharField(max_length=100, choices=TRIP)
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()


PACKAGE_TYPES = (
    ('group', 'group'),
    ('custom', 'custom'),
)
class Package(models.Model):
    """Slots for group are read only, for custom is number of editable """
    type = models.CharField(max_length=100, choices=PACKAGE_TYPES)
    category = models.ForeignKey(PackageCategory, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    slots = models.PositiveIntegerField(default=0)
    start = models.DateField()
    end = models.DateField()
    price = models.PositiveIntegerField()
    activities = models.CharField(max_length=200, choices=PACKAGE_TYPES)
    arrival_accomodation = models.ForeignKey(Accomadation, on_delete=models.CASCADE, related_name="arrival_accom")
    trip_accomodation = models.ForeignKey(Accomadation, on_delete=models.CASCADE, related_name="trip_accom")
    pickup = models.CharField(max_length=100)
    dropoff = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    class Meta :
       ordering = ['-id']

    def __str__(self):
        return f"{self.type} "


class Flight(models.Model):
    start = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    class Meta :
       ordering = ['-id']

    # def all_verified(self):
    #     print(self.approved)
    #     return self.approved

    def __str__(self):
        return f"{self.start} - {self.destination}"


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    departure_date = models.DateField(max_length=100)
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    infants = models.PositiveIntegerField()

    class Meta :
       ordering = ['-id']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.flight}"





