from django.db import models
from django.db.models.base import Model
from hostels.models import Hostel
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activity_type = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200, null=True)
    activity = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)


class ChatRoom(models.Model):
    person_1 = models.ForeignKey(User, on_delete=models.CASCADE)
    person_2 = models.IntegerField()


class Message(models.Model):
    room_id = models.OneToOneField(ChatRoom, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(max_length=20, null=True)
