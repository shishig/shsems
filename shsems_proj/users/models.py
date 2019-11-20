from django.db import models
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
   contact_number = models.CharField("Contact Number",
      max_length = 50)
   designation = models.ForeignKey(to = "Designation", 
      on_delete = models.SET_NULL, blank = True, null = True)
      
class Designation(models.Model):
   name = models.CharField("Designation", max_length=50)

   
   
