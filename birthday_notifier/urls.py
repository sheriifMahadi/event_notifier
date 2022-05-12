from ast import Add
from unicodedata import name
from django import views
from django.urls import path
from .views import EditEvent, DeleteEventView, EventDetailView, EventListView, AddEvent, EditEvent


app_name = 'main'
urlpatterns = [
    path('', EventListView.as_view(), name='events'), 
    path('celebrant/<slug:slug>', EventDetailView.as_view(), name='detail'),
    path('new_event', AddEvent, name='new_event'), 
    path('edit_event/<slug:slug>', EditEvent, name='edit_event'), 
    path('delete/<slug:slug>', DeleteEventView.as_view(), name='delete')
    
]
