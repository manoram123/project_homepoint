# Generated by Django 3.2.4 on 2021-08-15 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_address'),
        ('user', '0017_auto_20210815_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='person_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]
