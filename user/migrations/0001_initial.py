# Generated by Django 3.2.4 on 2021-08-08 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('activity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostels.hostel')),
            ],
        ),
    ]