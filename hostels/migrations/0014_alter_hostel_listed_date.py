# Generated by Django 3.2.4 on 2021-08-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0013_alter_hostel_listed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='listed_date',
            field=models.DateField(null=True),
        ),
    ]
