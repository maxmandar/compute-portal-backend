# Generated by Django 4.1.7 on 2023-03-03 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bom', '0003_opensystemsintelvirtualserverconfiguration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('service_description', models.TextField()),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('configuration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professional_services', to='bom.opensystemsintelvirtualserverconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='AdhocPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_name', models.CharField(max_length=255)),
                ('price_description', models.TextField()),
                ('price_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('configuration', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='adhoc_prices', to='bom.opensystemsintelvirtualserverconfiguration')),
            ],
        ),
    ]
