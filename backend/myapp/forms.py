from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Accomadation, Activity, Booking, Car, Flight, Gallery, Trip, PackageCategory, CarHire
import datetime
from django.forms import Form, ModelForm, DateField, widgets


class TripForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=PackageCategory.objects.all(), empty_label='Select package category')
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Trip destination'}))
    arrival_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation on arrival')
    trip_accomodation = forms.ModelChoiceField(queryset=Accomadation.objects.all(), empty_label='Select  accomodation at trip destination')
    pickup = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pickup location'}))
    dropoff = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Drop off location'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))
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
        exclude = ('id', )
        


class GoupTripBookingForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))
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
        exclude = ('id', 'car_hire', 'flight', 'flight_type', 'departure_date', 'adults', 'children', 'infants')
        # widgets = {
        # 'trip': forms.TextInput(attrs={'readonly': 'readonly'}),
        # }
     