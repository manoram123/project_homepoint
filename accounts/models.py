from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True),
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='static/users', null=True,
                              default='static/users/default.jpg')
    active_status = models.BooleanField()
    verified = models.BooleanField()
