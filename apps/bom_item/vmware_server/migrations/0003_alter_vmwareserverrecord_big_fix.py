# Generated by Django 4.1.7 on 2023-05-12 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vmware_server', '0002_bigfixnew_alter_vmwareserverrecord_big_fix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmwareserverrecord',
            name='big_fix',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vmware_server.bigfix'),
        ),
    ]