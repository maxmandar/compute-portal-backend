# Generated by Django 4.1.7 on 2023-03-07 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructureinitiationdocument', '0007_alter_iidrequestor_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='iidrequestor',
            name='iid_project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='infrastructureinitiationdocument.iidproject'),
            preserve_default=False,
        ),
    ]
