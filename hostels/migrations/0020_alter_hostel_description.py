# Generated by Django 3.2.4 on 2021-08-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0019_services_laundry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
