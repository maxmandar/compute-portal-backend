# Generated by Django 4.1.7 on 2023-05-13 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billofmaterial', '0006_billofmaterial_project'),
        ('infrastructureinitiationdocument', '0014_alter_iidrequestor_requestor'),
        ('vmware_server', '0008_alter_vmwareserversizecost_cost_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='vmware_server',
        ),
        migrations.RemoveField(
            model_name='bigfixconfig',
            name='vmware_server',
        ),
        migrations.RemoveField(
            model_name='bigfixcost',
            name='big_fix_config',
        ),
        migrations.AddField(
            model_name='vmwareserver',
            name='application',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.application'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vmwareserver',
            name='bom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='billofmaterial.billofmaterial'),
        ),
        migrations.AlterField(
            model_name='vmwareserver',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='infrastructureinitiationdocument.iidproject'),
        ),
        migrations.CreateModel(
            name='BigFix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_fix_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_fixes', to='vmware_server.bigfixconfig')),
                ('big_fix_cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='big_fixes', to='vmware_server.bigfixcost')),
            ],
        ),
        migrations.AddField(
            model_name='vmwareserver',
            name='big_fix',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vmware_servers', to='vmware_server.bigfix'),
            preserve_default=False,
        ),
    ]
