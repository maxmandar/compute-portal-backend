# Generated by Django 4.1.7 on 2023-04-12 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricebook', '0013_rename_vmwareservercost_virtualservercost_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='osstorage',
            name='costs',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='costs',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='hypervisor',
        ),
        migrations.RemoveField(
            model_name='virtualmachine',
            name='os_storage',
        ),
        migrations.DeleteModel(
            name='Hypervisor',
        ),
        migrations.DeleteModel(
            name='OsStorage',
        ),
        migrations.DeleteModel(
            name='VirtualMachine',
        ),
    ]
