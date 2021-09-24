from django.db import models
from django.contrib.auth.models import User, update_last_login
from django.core import validators


# Create your models here.


class Services(models.Model):
    internet = models.BooleanField()
    parking = models.BooleanField()
    water = models.BooleanField()
    additional_s = models.TextField(max_length=1000, null=True)


class Rules(models.Model):
    dog_friendly = models.BooleanField()
    cat_friendly = models.BooleanField()
    smoking_allowed = models.BooleanField()
    additional_r = models.TextField(max_length=1000)


class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    price = models.IntegerField()
    home_type = models.CharField(max_length=100, null=True)
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


class HomeRenting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    date = models.DateField()
    member = models.PositiveBigIntegerField(validators=[
        validators.MaxValueValidator(5),
        validators.MinValueValidator(1)
    ])
    adult = models.PositiveIntegerField(null=True, validators=[
        validators.MaxValueValidator(3),
        validators.MinValueValidator(1)
    ])
    child = models.PositiveIntegerField(null=True, validators=[
        validators.MaxValueValidator(2),
        validators.MinValueValidator(1)
    ])
    is_paid = models.BooleanField(default=False, null=True)
    duration = models.IntegerField(null=True, validators=[
        validators.MaxValueValidator(3),
        validators.MinValueValidator(1)
    ])
