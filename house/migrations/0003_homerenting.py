# Generated by Django 3.2.4 on 2021-09-13 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0002_auto_20210912_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeRenting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('member', models.PositiveIntegerField()),
                ('adult', models.PositiveIntegerField(null=True)),
                ('child', models.PositiveIntegerField(null=True)),
                ('is_paid', models.BooleanField(default=False, null=True)),
                ('duration', models.IntegerField(null=True)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.home')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
