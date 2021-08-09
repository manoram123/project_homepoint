from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


class Hostel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    services = models.CharField(max_length=50)
    rules = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    availability = models.BooleanField(null=True)
    image1 = models.FileField(upload_to='static/uploads')
    image2 = models.FileField(upload_to='static/uploads')
    image3 = models.FileField(upload_to='static/uploads')
    image4 = models.FileField(upload_to='static/uploads')
    image5 = models.FileField(upload_to='static/uploads')
    image6 = models.FileField(upload_to='static/uploads')
