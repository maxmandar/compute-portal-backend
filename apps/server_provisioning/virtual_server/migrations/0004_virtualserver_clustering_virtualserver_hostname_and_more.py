# Generated by Django 4.1.7 on 2023-04-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_server', '0003_remove_virtualserver_clustering_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualserver',
            name='clustering',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='hostname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='model',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='platform',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]