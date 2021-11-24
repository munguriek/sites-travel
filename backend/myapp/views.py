from django.shortcuts import get_object_or_404, render

from .models import Flight, Package
from . import *

# Create your views here.
def group_packages(request):
    packages = Package.objects.filter(type='group')
    print(packages.count())
    context = {'group_packages': packages}
    return render(request, "packages-group.html", context)


def custom_packages(request):
    context = {}
    return render(request, "packages-custom.html", context)


def flights(request):
    flights = Flight.objects.all()
    print(flights)
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
    context = {}
    return render(request, "cars.html", context)


def gallery(request):
    context = {}
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