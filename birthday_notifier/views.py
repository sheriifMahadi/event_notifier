from urllib import request
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DeleteView, DetailView, ListView
from pyexpat import model

from .forms import EventForm
from .models import Event

User = settings.AUTH_USER_MODEL

class EventListView(ListView):
    model = Event
    template_name = 'birthday_notifier/events.html'
     
    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            events = Event.objects.filter(owner=self.request.user)
            return events       

class EventDetailView(DetailView):
    model = Event
    template_name = 'birthday_notifier/event_detail.html'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            events = Event.objects.filter(owner=self.request.user)
            return events

@login_required
def AddEvent(request):
    if request.method == "POST": 
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            new_event = event_form.save(commit=False)
            new_event.owner = request.user
            new_event.save()
            messages.success(request, ('A new event has been added'))
            return redirect("main:events")

        else: 
            messages.error(request, ('You are trying to add an existing event'))


    context = {
        "event_form": EventForm,
    }
    return render(request, "birthday_notifier/add_event.html", context)

@login_required
def EditEvent(request, slug): 
    event = Event.objects.get(slug=slug.lower())
    if event.owner != request.user: 
        raise Http404
    if request.method != 'POST':
        event_form = EventForm(instance=event)
    else:
        event_form = EventForm(instance=event, data=request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, ('Event has been edited'))
            return redirect ('main:detail', slug=slug.lower())
        
        else: 
            messages.error(request, ('Failed to edit event. Try again'))

    context = {'event_form': event_form, 'event': event}
    return render(request, "birthday_notifier/add_event.html", context)

class DeleteEventView(DeleteView):
    model = Event
    slug_url_kwarg = 'slug'
    template_name = 'birthday_notifier/confirm_delete.html'
    success_url = "/"
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            events = Event.objects.filter(owner=self.request.user)
            return events
