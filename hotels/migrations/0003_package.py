# Generated by Django 3.2.4 on 2021-09-20 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_remove_hotels_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_title', models.CharField(max_length=500)),
                ('price', models.PositiveBigIntegerField()),
                ('features', models.CharField(max_length=1000)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotels')),
            ],
        ),
    ]
