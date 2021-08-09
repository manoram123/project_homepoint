from django.db import models
from django.db.models.base import Model
from hostels.models import Hostel
from django.contrib.auth.models import User

# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activity_type = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200, null=True)
    activity = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
