# Generated by Django 3.2.4 on 2021-09-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booked_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_in_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(null=True),
        ),
    ]