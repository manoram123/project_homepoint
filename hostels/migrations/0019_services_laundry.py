# Generated by Django 3.2.4 on 2021-08-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0018_alter_hostel_listed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='laundry',
            field=models.BooleanField(null=True),
        ),
    ]
