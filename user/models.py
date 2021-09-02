from io import open_code
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
    person_1 = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    person_2 = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(max_length=20, null=True)
    reply_on = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    Notification = models.CharField(max_length=1000)
    is_seen = models.BooleanField(default=False)
