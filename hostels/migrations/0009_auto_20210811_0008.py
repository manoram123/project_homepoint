# Generated by Django 3.2.4 on 2021-08-10 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hostels', '0008_rename_gayser_services_geyser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='hostel_p',
        ),
        migrations.AddField(
            model_name='hostel',
            name='services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hostels.services'),
        ),
    ]
