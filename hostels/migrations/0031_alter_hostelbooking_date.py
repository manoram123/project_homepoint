# Generated by Django 3.2.4 on 2021-09-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0030_alter_hostelbooking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelbooking',
            name='date',
            field=models.DateField(),
        ),
    ]
