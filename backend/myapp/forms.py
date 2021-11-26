from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Accomadation, Activity, Car, Flight, Gallery, Package, PackageCategory, Ticket, Transport
import datetime
from django.forms import Form, ModelForm, DateField, widgets


class PackageForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=PackageCategory.objects.all(), empty_label='Select package category')
    # type = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter type'}))

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        self.fields['type'].label = "Package type"

    def clean_date(self):
        date = self.cleaned_data['date']
        if self.start < datetime.date.today():
            raise forms.ValidationError("Book only dates in the future!")
        return date

    class Meta:
        model = Package
        fields = '__all__'
        exclude = ('id', )   
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'})
        } 


class FlightForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        # self.fields['batch'].label = "Batch number"

    class Meta:
        model = Flight
        fields = '__all__'
        exclude = ('id', )   
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'})
        }


class CarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        # self.fields['batch'].label = "Batch number"
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('id', )   
     

class GalleryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        # self.fields['batch'].label = "Batch number"
    class Meta:
        model = Gallery
        fields = '__all__'
        exclude = ('id', )   
     