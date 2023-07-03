# Generated by Django 4.1.7 on 2023-03-01 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_approved', to='employee.employee')),
                ('project_managers', models.ManyToManyField(related_name='projects_managed', to='employee.employee')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_requested', to='employee.employee')),
                ('verifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_verified', to='employee.employee')),
            ],
        ),
    ]
