from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "events_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"

class MyEventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'my_events_list.html'

    def get_queryset(self):
        return Event.objects.filter(creator = self.request.user)