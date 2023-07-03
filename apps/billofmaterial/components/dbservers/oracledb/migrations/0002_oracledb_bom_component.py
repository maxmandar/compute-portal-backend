# Generated by Django 4.1.7 on 2023-03-04 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billofmaterial', '0002_billofmaterialcomponent'),
        ('oracledb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oracledb',
            name='bom_component',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oracle_db', to='billofmaterial.billofmaterialcomponent'),
        ),
    ]
