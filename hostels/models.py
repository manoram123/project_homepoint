from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Services(models.Model):
    internet = models.BooleanField()
    breakfast = models.BooleanField()
    gym = models.BooleanField()
    geyser = models.BooleanField()
    parking = models.BooleanField()
    additional_s = models.CharField(max_length=1000, null=True)


class Hostel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    services = models.ForeignKey(Services, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=1000)
    availability = models.BooleanField(null=True)
    listed_date = models.DateField(max_length=20, null=True)
    image1 = models.FileField(upload_to='static/uploads')
    image2 = models.FileField(upload_to='static/uploads')
    image3 = models.FileField(upload_to='static/uploads')
    image4 = models.FileField(upload_to='static/uploads')
    image5 = models.FileField(upload_to='static/uploads')
    image6 = models.FileField(upload_to='static/uploads')


class rules(models.Model):
    hostel_r = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    dog_friendly = models.BooleanField()
    cat_friendly = models.BooleanField()
    additional_r = models.CharField(max_length=1000)
