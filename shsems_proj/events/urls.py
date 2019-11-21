from django.urls import path

from .views import EventListView, EventDetailView, MyEventListView,MyEventCreateView, EventUpdateView, EventDeleteView, EventShowParticipantView


urlpatterns = [
    path('all/', EventListView.as_view(),name = "events_list"),
    path('new/',MyEventCreateView.as_view(), name = "create_event"),
    path('<int:pk>/', EventDetailView.as_view(), name = "event_detail"),
    path('my_event/', MyEventListView.as_view(), name = "my_events_list"),
    path('edit/<int:pk>', EventUpdateView.as_view(), name = "edit"),
    path('delete/<int:pk>', EventDeleteView.as_view(), name = "delete"),
    path('show/<int:pk>', EventShowParticipantView.as_view(), name = "show"),

]
