from django.urls import path
from .views import RegistrationCreateView

urlpatterns= [
    path("new/<int:event_pk>", RegistrationCreateView.as_view(), name="registration_create")
]