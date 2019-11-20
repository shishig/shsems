from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "events_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"