from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.utils import tree


class Services(models.Model):
    internet = models.BooleanField()
    breakfast = models.BooleanField()
    gym = models.BooleanField()
    geyser = models.BooleanField()
    parking = models.BooleanField()
    laundry = models.BooleanField(null=True)
    additional_s = models.TextField(max_length=1000, null=True)


class Rules(models.Model):
    dog_friendly = models.BooleanField()
    cat_friendly = models.BooleanField()
    additional_r = models.TextField(max_length=1000)


class Hostel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    price = models.IntegerField()
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    rules = models.ForeignKey(Rules, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000)
    availability = models.BooleanField(null=True)
    listed_date = models.DateField(max_length=20, null=True)
    image1 = models.FileField(upload_to='static/uploads')
    image2 = models.FileField(upload_to='static/uploads')
    image3 = models.FileField(upload_to='static/uploads')
    image4 = models.FileField(upload_to='static/uploads')
    image5 = models.FileField(upload_to='static/uploads')
    image6 = models.FileField(upload_to='static/uploads')
    rating = models.IntegerField(null=True)
