from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Services(models.Model):
    internet = models.BooleanField()
    breakfast = models.BooleanField()
    parking = models.BooleanField()
    additional_s = models.TextField(max_length=1000, null=True)


class Rules(models.Model):
    dog_friendly = models.BooleanField()
    cat_friendly = models.BooleanField()
    smoking_allowed = models.BooleanField()
    additional_r = models.TextField(max_length=1000)


class Hotels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
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


class Package(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    package_title = models.CharField(max_length=500)
    price = models.PositiveBigIntegerField()
    type_of_stay = models.CharField(max_length=200, null=True)
    features = models.CharField(max_length=1000)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    check_in_date = models.CharField(null=True, max_length=100)
    check_out_date = models.CharField(null=True, max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    adults = models.PositiveBigIntegerField()
    child = models.PositiveBigIntegerField()
    days_of_stay = models.PositiveBigIntegerField()
    booked_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True)
