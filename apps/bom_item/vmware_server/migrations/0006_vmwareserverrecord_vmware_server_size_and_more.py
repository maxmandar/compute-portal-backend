# Generated by Django 4.1.7 on 2023-05-12 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vmware_server', '0005_vmwareserverrecord_vmware_server_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmwareserverrecord',
            name='vmware_server_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vmware_server.vmwareserversize'),
        ),
        migrations.AlterField(
            model_name='vmwareserverrecord',
            name='big_fix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vmware_server.bigfix'),
        ),
    ]
