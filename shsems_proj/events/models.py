from django.db import models

class Event(models.Model):
    name = models.CharField("Name of Event", max_length = 150, blank=False, null=False)
    description = models.TextField("Desciption", max_length=2000, blank = True, null = True)
    max_slots = models.IntegerField("Max Slots", blank=True, null=True)
    date_from = models.DateField("Start Date")
    date_to = models.DateField("End Date")
    time_from = models.TimeField("Start Time")
    time_to = models.TimeField("End Time")
    creator = models.ForeignKey(to = "users.Participant", on_delete = models.CASCADE)

    def __str__(self):
        return self.name