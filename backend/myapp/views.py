from django.shortcuts import get_object_or_404, render
from .models import Flight, Gallery, Package, Transport, Car, Ticket, Accomadation
from . import *
from django.contrib import messages


# Create your views here.
def group_packages(request):
    packages = Package.objects.filter(type='group')
    messages.success(request, "Thanks") 
    context = {
        'group_packages': packages,
    }
    return render(request, "packages-group.html", context)


def custom_packages(request):
    context = {}
    return render(request, "packages-custom.html", context)


def flights(request):
    flights = Flight.objects.all()
    context = {"flights": flights}
    return render(request, "flights.html", context)

def flight(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    print(flight)
    context = {"flight": flight}
    return render(request, "flights.html", context)

def ticketing(request):
    context = {}
    return render(request, "ticketing.html", context)


def cars(request):
    cars = Car.objects.all()
    transport = Transport.objects.all()
    messages.success(request, "Thanks")
    context = {"cars": cars}
    return render(request, "cars.html", context)


def gallery(request):
    pictures = Gallery.objects.all()
    context = {"pictures": pictures}
    return render(request, "gallery.html", context)


def blog_list(request):
    context = {}
    return render(request, "blog_list.html", context)

def blog_detail(request):
    context = {}
    return render(request, "blog_detail.html", context)


def contacts(request):
    context = {}
    return render(request, "contacts.html", context)



# Admin
def main(request):
    """Index page for admin panel."""
    group_packages = Package.objects.filter(type="group").count()
    custom_packages = Package.objects.filter(type="custom").count()

    accom_budget = Accomadation.objects.filter(budget="budget").count()
    accom_mid_range = Accomadation.objects.filter(budget="mid range").count()
    accom_up_market = Accomadation.objects.filter(budget="up market").count()

    trans_budget = Transport.objects.filter(budget="budget").count()
    trans_mid_range = Transport.objects.filter(budget="mid range").count()
    trans_up_market = Transport.objects.filter(budget="up market").count()

    trans_driver = Transport.objects.filter(driver="driver").count()
    trans_self = Transport.objects.filter(driver="self").count()

    trans_town = Transport.objects.filter(driver="town service").count()
    trans_upcountry = Transport.objects.filter(driver="upcountry").count()

    one_way_tickets = Ticket.objects.filter(type="town service").count()
    return_tickets = Ticket.objects.filter(type="upcountry").count()

    context = {
            "group_packages": group_packages,
            "custom_packages": custom_packages,
            "accom_budget" : accom_budget,
            "accom_mid_range": accom_mid_range,
            "accom_up_market": accom_up_market,
            "trans_budget" : trans_budget,
            "trans_mid_range": trans_mid_range,
            "trans_up_market": trans_up_market,
            "trans_driver": trans_driver,
            "trans_self": trans_self,
            "trans_town": trans_town,
            "trans_upcountry": trans_upcountry,
            "one_way_tickets": one_way_tickets,
            "return_tickets": return_tickets,
    }
    return render(request, "admin/main.html", context) 

def packages(request):
    packages = Package.objects.all()
    messages.success(request, "Thanks") 
    context = {
        'packages': packages,
    }
    return render(request, "admin/packages.html", context)

