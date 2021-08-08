from django.db import models


class Hostel(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    price = models.IntegerField()
    services = models.CharField(max_length=500)
    rules = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    image1 = models.FileField(upload_to='static/uploads')
    image2 = models.FileField(upload_to='static/uploads')
    image3 = models.FileField(upload_to='static/uploads')
    image4 = models.FileField(upload_to='static/uploads')
    image5 = models.FileField(upload_to='static/uploads')
    image6 = models.FileField(upload_to='static/uploads')
