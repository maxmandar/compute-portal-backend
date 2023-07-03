# Generated by Django 4.1.7 on 2023-03-02 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pricebook', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VMwareServerSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=250)),
                ('vcpu', models.IntegerField()),
                ('ram_gb', models.IntegerField()),
                ('server_cost_CE', models.IntegerField()),
                ('hypervisor_cost_CE', models.IntegerField()),
                ('windows_os_cost_AS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('cost_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pricebook.costtype')),
            ],
        ),
    ]