from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .forms import ParticipantCreationForm

class ParticipantCreateView(CreateView):
    form_class = ParticipantCreationForm
    template_name = 'signup.html'
    success_url = 'login'

class HomePageView(TemplateView):
   template_name = 'home.html'

