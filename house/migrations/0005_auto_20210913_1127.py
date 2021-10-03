# Generated by Django 3.2.4 on 2021-09-13 05:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_alter_homerenting_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homerenting',
            name='adult',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='homerenting',
            name='child',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)]),
        ),
    ]