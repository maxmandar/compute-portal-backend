# Generated by Django 4.1.7 on 2023-05-13 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vmware_server', '0010_remove_vmwareserversizeconfig_vmware_server_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmwareserver',
            name='big_fix',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.bigfix'),
        ),
    ]
