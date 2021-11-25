from django.shortcuts import get_object_or_404, render
from .models import Flight, Gallery, Package, Transport, Car
from . import *
from django.contrib import messages


# Create your views here.
def group_packages(request):
    packages = Package.objects.filter(type='group')
    messages.success(request, "Thanks") 
    context = {'group_packages': packages}
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