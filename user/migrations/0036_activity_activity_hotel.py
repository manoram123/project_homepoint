# Generated by Django 3.2.4 on 2021-09-15 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
        ('user', '0035_message_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels'),
        ),
    ]
