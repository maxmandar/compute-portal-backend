# Generated by Django 4.1.7 on 2023-03-01 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iid', '0009_alter_iid_approver_alter_iid_requestor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segment',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
