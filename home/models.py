from django.db import models
from django.db.models.fields import DateField
from hostels.models import Hostel
from django.contrib.auth.models import User

# Create your models here.


class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    # hotel = models.ForeignKey()
    # home = models.ForeignKey()
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
