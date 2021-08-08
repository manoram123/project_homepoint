from django.db import models
from django.db.models.base import Model
from hostels.models import Hostel

# Create your models here.


class Activity(models.Model):
    activity_type = models.CharField(max_length=200)
    activity_id = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
