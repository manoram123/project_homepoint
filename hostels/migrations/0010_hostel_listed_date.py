# Generated by Django 3.2.4 on 2021-08-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0009_auto_20210811_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='listed_date',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
