# Generated by Django 4.1.7 on 2023-03-01 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('iid', '0006_iid_requestor_iid_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='iid',
            name='approver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='iid_approver', to='employee.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iid',
            name='reviewer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='iid_reviewer', to='employee.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iid',
            name='verifier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='iid_verifier', to='employee.employee'),
            preserve_default=False,
        ),
    ]
