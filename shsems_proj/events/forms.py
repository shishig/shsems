from django.forms import ModelForm

from .models import Event

class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name","description","max_slots","date_from","date_to","time_from","time_to")
        
class EventUpdateForm(ModelForm):
    class Meta:
       model = Event
       fields = ("description", "max_slots","date_to","time_from","time_to")

class EventDeleteForm(ModelForm):
    class Meta:
        model = Event
        fields = ("name","description","max_slots","date_from","date_to","time_from","time_to")
