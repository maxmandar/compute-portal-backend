# Generated by Django 4.1.7 on 2023-05-13 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vmware_server', '0012_remove_vmwareserversize_vmware_server_size_cost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmwareserver',
            name='big_fix',
        ),
        migrations.RemoveField(
            model_name='vmwareserver',
            name='vmmware_server_size',
        ),
        migrations.AddField(
            model_name='vmwareserver',
            name='big_fix_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.bigfixconfig'),
        ),
        migrations.AddField(
            model_name='vmwareserver',
            name='big_fix_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.bigfixcost'),
        ),
        migrations.AddField(
            model_name='vmwareserver',
            name='vmmware_server_size_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.vmwareserversizeconfig'),
        ),
        migrations.AddField(
            model_name='vmwareserver',
            name='vmmware_server_size_cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.vmwareserversizecost'),
        ),
    ]
