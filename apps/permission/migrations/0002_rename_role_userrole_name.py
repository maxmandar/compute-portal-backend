# Generated by Django 4.1.7 on 2023-05-24 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrole',
            old_name='role',
            new_name='name',
        ),
    ]
