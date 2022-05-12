from tkinter import Widget
from django import forms

from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event 
        fields = ('celebrant', 'birthdate')
        widgets = {
            'birthdate': forms.DateTimeInput(attrs={'type': 'date'})
        }
