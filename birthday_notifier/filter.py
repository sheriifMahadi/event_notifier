
import django_filters
from .models import Event
from django_filters import DateFilter
from django import forms


class Search(django_filters.FilterSet):
    event = django_filters.CharFilter(lookup_expr='icontains', 
                                        widget=forms.TextInput(attrs={'placeholder': "Search for an event", 'class':'search'}))
        
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['date_added']