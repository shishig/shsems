from django.urls import path

from .views import EventListView, EventDetailView, MyEventListView


urlpatterns = [
    path('all/', EventListView.as_view(),name = "events_list"),
    path('<int:pk>/', EventDetailView.as_view(),name = "event_detail"),
    path('my_event/', MyEventListView.as_view(),name = "my_events_list"),
]