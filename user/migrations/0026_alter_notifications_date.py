# Generated by Django 3.2.4 on 2021-09-10 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_chatroom_hostel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
