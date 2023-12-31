# Generated by Django 4.1.7 on 2023-04-21 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtual_server', '0006_virtualserversize_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HypervisorCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkPortCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ServerCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cost_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='virtualserver',
            name='cost',
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='hypervisor_cost',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='virtual_server.hypervisorcost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='network_port_cost',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='virtual_server.networkportcost'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='virtualserver',
            name='server_cost',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='virtual_server.servercost'),
            preserve_default=False,
        ),
    ]
