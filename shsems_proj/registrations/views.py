from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Registration
from events.models import Event


class RegistrationCreateView(LoginRequiredMixin, CreateView):
    model = Registration
    template_name = "registration.html"
    fields = ("waiver","parents_permit","parents_contact_number",)
    success_url = reverse_lazy('events_list')

    def form_valid(self, form):
        form.instance.event = Event.objects.filter(pk=self.kwargs['event_pk']).first()
        form.instance.participant = self.request.user
        return super().form_valid(form)



