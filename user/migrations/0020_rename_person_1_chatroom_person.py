# Generated by Django 3.2.4 on 2021-08-15 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_chatroom_person_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroom',
            old_name='person_1',
            new_name='person',
        ),
    ]
