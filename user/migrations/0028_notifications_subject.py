# Generated by Django 3.2.4 on 2021-09-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_alter_notifications_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='subject',
            field=models.IntegerField(null=True),
        ),
    ]
