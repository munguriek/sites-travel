from django.contrib import admin
from .models import Accomadation, Activity, Car, CarHire, Flight, Gallery, Trip, PackageCategory, Booking

# Register your models here.
admin.site.register(Accomadation)
admin.site.register(PackageCategory)
admin.site.register(Activity)
admin.site.register(Trip)
admin.site.register(Flight)
admin.site.register(Car)
admin.site.register(CarHire)
admin.site.register(Gallery)
admin.site.register(Booking)
