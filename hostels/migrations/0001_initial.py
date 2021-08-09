# Generated by Django 3.2.4 on 2021-08-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('services', models.CharField(max_length=500)),
                ('rules', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('image1', models.FileField(upload_to='static/uploads')),
                ('image2', models.FileField(upload_to='static/uploads')),
                ('image3', models.FileField(upload_to='static/uploads')),
                ('image4', models.FileField(upload_to='static/uploads')),
                ('image5', models.FileField(upload_to='static/uploads')),
                ('image6', models.FileField(upload_to='static/uploads')),
            ],
        ),
    ]