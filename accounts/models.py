from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='static/users', null=True,
                              default='static/users/default.jpg')
    active_status = models.BooleanField()
    verified = models.BooleanField()

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path
