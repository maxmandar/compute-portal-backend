# Generated by Django 4.1.7 on 2023-03-07 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('infrastructureinitiationdocument', '0004_iidrequestor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iidrequestor',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]