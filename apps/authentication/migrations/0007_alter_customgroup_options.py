# Generated by Django 4.1.7 on 2023-03-09 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customgroup',
            options={'verbose_name': 'Custom Group'},
        ),
    ]
