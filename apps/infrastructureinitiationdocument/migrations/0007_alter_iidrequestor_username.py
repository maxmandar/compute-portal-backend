# Generated by Django 4.1.7 on 2023-03-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructureinitiationdocument', '0006_alter_iidrequestor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iidrequestor',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]