# Generated by Django 3.2.4 on 2021-08-08 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activity_id',
            new_name='activity',
        ),
    ]
