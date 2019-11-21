from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Event
from .forms import EventCreateForm, EventUpdateForm, EventDeleteForm
from django.urls import reverse_lazy

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

class MyEventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = "event_create.html"
    success_url = reverse_lazy("my_events_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = "event_update.html"
    success_url = reverse_lazy("my_events_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    form_class = EventDeleteForm
    template_name = "event_delete.html"
    success_url = reverse_lazy("my_events_list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


