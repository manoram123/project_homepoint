# Generated by Django 3.2.4 on 2021-09-08 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0029_rename_data_hostelbooking_date'),
        ('user', '0024_notifications_notification_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='hostel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hostels.hostel'),
        ),
    ]
