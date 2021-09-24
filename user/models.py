from hotels.models import Hotels
from io import open_code
from django.db import models
from django.db.models.base import Model
from hostels.models import Hostel
from house.models import Home
from django.contrib.auth.models import User
from accounts.models import Profile
from datetime import datetime
# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    activity_type = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200, null=True)
    activity = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)
    activity_home = models.ForeignKey(
        Home, on_delete=models.CASCADE, null=True)
    activity_hotel = models.ForeignKey(
        Hotels, on_delete=models.CASCADE, null=True)

    date = models.CharField(max_length=200)


class ChatRoom(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)
    # home = models.ForeignKey(Home, on_delete=models.CASCADE)
    # property = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    person_1 = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    person_2 = models.ForeignKey(User, on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.CharField(max_length=500, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(max_length=20, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    reply_on = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    Notification = models.CharField(max_length=1000, null=True)
    is_seen = models.BooleanField(default=False)
    notification_user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=500, null=True)
