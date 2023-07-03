# Generated by Django 4.1.7 on 2023-04-11 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricebook', '0008_networksku_description_pricebook_server_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmwareserversize',
            name='hypervisor_cost_CE',
        ),
        migrations.RemoveField(
            model_name='vmwareserversize',
            name='server_cost_CE',
        ),
        migrations.RemoveField(
            model_name='vmwareserversize',
            name='windows_os_cost_AS',
        ),
        migrations.CreateModel(
            name='VmwareServerCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vmware_server_cost_type', to='pricebook.costtype')),
                ('server_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vmware_server_cost', to='pricebook.vmwareserversize')),
            ],
        ),
        migrations.CreateModel(
            name='OsStorageCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storage_cost_type', to='pricebook.costtype')),
                ('server_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_cost', to='pricebook.vmwareserversize')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='network_cost_type', to='pricebook.costtype')),
                ('server_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_cost', to='pricebook.vmwareserversize')),
            ],
        ),
    ]
