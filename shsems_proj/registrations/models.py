from django.db import models
from users.models import Participant
from events.models import Event
from extras.utils import generate_random_string


def waiver_upload_path(instance, filename):
    return "waiver/{}-{}".format(generate_random_string(10), filename)

def permit_upload_path(instance, filename):
    return "permit/{}-{}".format(generate_random_string(10), filename)

class Registration(models.Model):
    
    class Meta:
        unique_together = ("event","participant")

    event = models.ForeignKey(to = "events.Event", on_delete = models.CASCADE)
    participant = models.ForeignKey(to = "users.Participant", on_delete = models.CASCADE)
    waiver = models.FileField("Waiver", upload_to=waiver_upload_path)
    parents_permit = models.FileField("Parent's Permit", upload_to=permit_upload_path)
    parents_contact_number = models.CharField("Parent's Contact Number", max_length=20)
    datetime_registered = models.DateTimeField("Date Registered", auto_now_add = True)
    status = models.CharField("Status", max_length=1, default="A")

