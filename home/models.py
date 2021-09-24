from django.db import models
from django.db.models.fields import DateField
from hostels.models import Hostel
from hotels.models import Hotels
from house.models import Home
from django.contrib.auth.models import User

# Create your models here.


class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True)
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=True)
    ratings = models.IntegerField()
    comment = models.TextField(max_length=1000, null=True)
    likes = models.IntegerField(default=0, null=True)
    date = models.DateField(null=True)


class Replies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Ratings, on_delete=models.CASCADE)
    reply = models.TextField(max_length=1000, null=True)
    likes = models.IntegerField(null=True)
    date = models.DateField()
