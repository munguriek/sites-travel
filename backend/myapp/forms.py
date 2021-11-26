from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.forms import ModelForm, DateInput
from .models import Accomadation, Activity, Car, Flight, Gallery, Package, PackageCategory, Ticket, Transport
import datetime
from django.forms import Form, ModelForm, DateField, widgets



# class BatchForm(forms.ModelForm):
#     drug = forms.ModelChoiceField(queryset=Vaccine.objects.filter(approved=True), empty_label='Select from list of vaccines')
#     batch = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter batch number of drug'}))
#     serial = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter serial number of drug'}))

#     def __init__(self, *args, **kwargs):
#         super(BatchForm, self).__init__(*args, **kwargs)
#         self.fields['batch'].label = "Batch number"
#         self.fields['serial'].label = "Serial number"
#         self.fields['drug'].label = "Vaccine Name"

#     def clean_date(self):
#         date = self.cleaned_data['date']
#         if self.expiry < datetime.date.today():
#             raise forms.ValidationError("Expiry date cannot be in the past!")
#         return date

#     class Meta:
#         model = Batch
#         fields = '__all__'
#         exclude = ('approved', 'added_by', )   
#         widgets = {
#             'expiry': widgets.DateInput(attrs={'type': 'date'})
#         } 


class PackageForm(forms.ModelForm):
    # drug = forms.ModelChoiceField(queryset=Package.objects.filter(approved=True), empty_label='Select from list of vaccines')
    # batch = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter batch number of drug'}))

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        # self.fields['batch'].label = "Batch number"

    # def clean_date(self):
    #     date = self.cleaned_data['date']
    #     if self.expiry < datetime.date.today():
    #         raise forms.ValidationError("Expiry date cannot be in the past!")
    #     return date

    class Meta:
        model = Package
        fields = '__all__'
        exclude = ('approved', 'added_by', )   
        widgets = {
            'start': widgets.DateInput(attrs={'type': 'date'}),
            'end': widgets.DateInput(attrs={'type': 'date'})
        } 