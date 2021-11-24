from django.contrib import admin
from .models import Accomadation, Activity, Car, Flight, Gallery, Package, PackageCategory, Ticket, Transport

# Register your models here.
admin.site.register(Accomadation)
admin.site.register(PackageCategory)
admin.site.register(Activity)
admin.site.register(Transport)
admin.site.register(Package)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Car)
admin.site.register(Gallery)