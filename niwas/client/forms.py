from django import forms
from django.forms import ModelForm

from hostupload.models import *


class DetailForm(forms.Form):
    place = forms.CharField(max_length=100)
    checkin = forms.DateField()

    checkout = forms.DateField()
    guests = forms.IntegerField()





class booking_form(ModelForm):
    class Meta:
        model = Booking_House
        fields = '__all__'



class booking_form(ModelForm):
    class Meta:
        model = Booking_Hostel
        fields = '__all__'

