from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Accomadation, Activity, Booking, Car, Driver, Flight, Gallery, Trip, PackageCategory
import datetime
from django.forms import Form, ModelForm, DateField, widgets
from django_countries.widgets import CountrySelectWidget


class TripForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=PackageCategory.objects.all(), empty_label='Select package category')
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Trip destination'}))
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation on arrival')
    trip_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation at trip destination')
    pickup = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pickup location'}))
    dropoff = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Drop off location'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your full name'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your nationality'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your phone number'}))


    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields['type'].label = "Package type"
        self.fields['destination'].label = "Trip destination"
        self.fields['image'].label = "Upload image(formats .png, .jpeg, jpg)"
        self.fields['slots'].placeholder = "Number of slots"
        self.fields['start'].label = "Start date of trip"
        self.fields['end'].label = "Start date of trip"
        self.fields['price'].placeholder = "Price(in Dollars)"


    def clean_date(self):
        date = self.cleaned_data['date']
        if self.start < datetime.date.today():
            raise forms.ValidationError("Book only dates in the future!")
        return date

    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ('id', )   
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'})
        } 


class FlightForm(forms.ModelForm):
    start = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Start location of flight '}))
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Destination of flight'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Price of flight'}))

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ('id', )   


class CarForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Make of car eg toyota'}))

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Upload image (formats .png, .jpeg, jpg)"

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('id', )   
     

class GalleryForm(forms.ModelForm):
    caption = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Caption uploaded image'}))

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
    class Meta:
        model = Gallery
        fields = '__all__'
        exclude = ('id', )   


class BookingForm(forms.ModelForm):
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select')
    # title = forms.CharField(initial = "Method 2 ")

    # caption = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Caption uploaded image'}))

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # self.fields['picture'].label = "Upload image (formats .png, .jpeg, jpg)"
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked',)
        


class GoupTripBookingForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your full name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email address'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your telephone number eg +25677125478511'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your nationality'}))
    pickup = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter location we can pick you for the trip'}))
    dropoff = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter a location we can drop you after trip'}))
    slots = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter number of trip participants'}))

    def __init__(self, *args, **kwargs):
        super(GoupTripBookingForm, self).__init__(*args, **kwargs)
        # self.fields['trip'].label = "Upload image (formats .png, .jpeg, jpg)"
        self.fields['trip'].disabled = True 
        self.fields['service'].disabled = True 
        

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'car_hire', 'flight', 'flight_type', 'departure_date', 'adults', 'children', 'infants')


class FlightBookingForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your full name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email address'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your telephone number eg +25677125478511'}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your nationality'}))
    slots = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter number of trip participants'}))

    def __init__(self, *args, **kwargs):
        super(FlightBookingForm, self).__init__(*args, **kwargs)
        self.fields['service'].disabled = True 
        self.fields['flight'].disabled = True 
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'car', 'start', 'end', 'trip', 'car_hire', 'pickup', 'dropoff', 'driven_by', 'carhire_trip')
        widgets = {
            'departure_date': widgets.DateInput(attrs={'type': 'date'}),
            'country': CountrySelectWidget()
        } 


class CarHireBookingForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your full name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your email address'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your telephone number eg +25677125478511'}))

    def __init__(self, *args, **kwargs):
        super(CarHireBookingForm, self).__init__(*args, **kwargs)
        self.fields['start'].label = "Pickup date"
        self.fields['end'].label = "Drop off date"
        self.fields['carhire_trip'].label = "Area of car trip"
        # self.fields['service'].disabled = True 
        
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('time_booked', 'flight', 'trip', 'flight_type', 'departure_date', 'pickup', 'dropoff',  'slots', 'adults', 'children', 'infants')
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'}),
        } 