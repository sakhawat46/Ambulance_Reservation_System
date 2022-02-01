from django import forms
from django.contrib.auth.models import User
from django.forms import fields, models
from learn_app.models import Reservation

class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget = forms.TextInput(attrs = {'type':'date'}))
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'type_of_ambulance', 'pickup_location', 'destination' ]

