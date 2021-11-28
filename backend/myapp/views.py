from django.shortcuts import get_object_or_404, render, redirect
from .models import Flight, Gallery, Trip, Car, CarHire, Accomadation, Booking
from .forms import (TripForm, FlightForm, CarForm, GalleryForm, BookingForm, GoupTripBookingForm, 
    FlightBookingForm, CarHireBookingForm) 
# CarForm, AccomadationForm
from . import *
from django.contrib import messages


# Create your views here.
def group_trips(request):
    trips = Trip.objects.filter(type='group')
    context = {
        'group_trips': trips,
    }
    return render(request, "packages-group.html", context)


def group_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)

    booking_form = GoupTripBookingForm(request.POST or None, request.FILES or None, 
        initial={"service": "trip", "trip": trip})
    if booking_form.is_valid():
        instance = booking_form.save(commit=False)
        instance.trip.slots = instance.trip.slots - instance.slots
        instance.trip.save()
        instance.save()       
        messages.success(request, 'Group trip booked successfully')
        return redirect('group_trips')
    context = {
        'trip': trip,
        'group_trip_booking': booking_form,
    }
    return render(request, "packages-group-detail.html", context)


def custom_trips(request):
    context = {}
    return render(request, "packages-custom.html", context)


def flight_list(request):
    flights = Flight.objects.all()
    context = {"flights": flights}
    return render(request, "flight-list.html", context)


def flight_detail(request, pk):
    flight = get_object_or_404(Flight, pk=pk)
    print(flight)

    booking_form = FlightBookingForm(request.POST or None, request.FILES or None, 
        initial={"service": "flight", "flight": flight })
    if booking_form.is_valid():
        instance = booking_form.save(commit=False)
        instance.save()       
        messages.success(request, 'Flight booked successfully')
        return redirect('flight_list')
    context = {
        'flight': flight,
        'booking_form': booking_form,
    }
    return render(request, "flight-detail.html", context)


def car_list(request):
    cars = Car.objects.all()
    car_hire = CarHire.objects.all()
    context = {"cars": cars}
    return render(request, "cars.html", context)


def gallery(request):
    pictures = Gallery.objects.filter(category="gallery")

    picture_form = GalleryForm(request.POST or None, request.FILES or None)
    if picture_form.is_valid():
        instance = picture_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Picture saved successfully')
        return redirect('gallery')
    context = {
        "pictures": pictures,
        "picture_form": picture_form,
    }
    return render(request, "gallery.html", context)


def blog_list(request):
    context = {}
    return render(request, "blog_list.html", context)

def blog_detail(request):
    context = {}
    return render(request, "blog_detail.html", context)


def contacts(request):
    return render(request, "contacts.html")



# Admin
def main(request):
    """Index page for admin panel."""
    trips = Trip.objects.all() 
    group_trips = trips.filter(type="group").count()
    custom_trips = trips.filter(type="custom").count()

    accomodation = Accomadation.objects.all()
    accom_budget = accomodation.filter(budget="budget").count()
    accom_midrange = accomodation.filter(budget="mid range").count()
    accom_upmarket = accomodation.filter(budget="up market").count()

    car_hires = CarHire.objects.all()
    carhire_budget = car_hires.filter(budget="budget").count()
    carhire_midrange = car_hires.filter(budget="mid range").count()
    carhire_upmarket = car_hires.filter(budget="up market").count()

    carhire_driver = car_hires.filter(driven_by="driver").count()
    carhire_self = car_hires.filter(driven_by="self").count()

    carhire_town = car_hires.filter(trip="town service").count()
    carhire_upcountry = car_hires.filter(trip="upcountry").count()

    bookings = Booking.objects.all()
    oneway_tickets = bookings.filter(flight_type="one way").count()
    return_tickets = bookings.filter(flight_type="return").count()

    context = {
            "group_trips": group_trips,
            "custom_trips": custom_trips,
            "accom_budget" : accom_budget,
            "accom_mid_range": accom_midrange,
            "accom_up_market": accom_upmarket,
            "carhire_budget" : carhire_budget,
            "carhire_midrange": carhire_midrange,
            "carhire_upmarket": carhire_upmarket,
            "carhire_driver": carhire_driver,
            "carhire_self": carhire_self,
            "carhire_town": carhire_town,
            "carhire_upcountry": carhire_upcountry,
            "oneway_tickets": oneway_tickets,
            "return_tickets": return_tickets,
    }
    return render(request, "admin/main.html", context) 


def packages(request):
    packages = Trip.objects.all()

    package_form = TripForm(request.POST or None, request.FILES or None)
    if package_form.is_valid():
        instance = package_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Package saved successfully')
        return redirect('packages')
    context = {
        'packages': packages,
        'package_form': package_form,
    }
    return render(request, "admin/packages.html", context)


def flights(request):
    flights = Flight.objects.all()

    flight_form = FlightForm(request.POST or None, request.FILES or None)
    if flight_form.is_valid():
        instance = flight_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Flight saved successfully')
        return redirect('flights')
    context = {
        'flights': flights,
        'flight_form': flight_form,
    }
    return render(request, "admin/flights.html", context)


def cars(request):
    cars = Car.objects.all()

    car_form = CarForm(request.POST or None, request.FILES or None)
    if car_form.is_valid():
        instance = car_form.save(commit=False)
        instance.save()                 
        messages.success(request, 'Car saved successfully')
        return redirect('cars')
    context = {
        'cars': cars,
        'car_form': car_form,
    }
    return render(request, "admin/cars.html", context)


