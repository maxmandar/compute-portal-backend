# Generated by Django 4.1.7 on 2023-03-07 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('infrastructureinitiationdocument', '0008_iidrequestor_iid_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iidrequestor',
            name='department',
        ),
        migrations.RemoveField(
            model_name='iidrequestor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='iidrequestor',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='iidrequestor',
            name='title',
        ),
        migrations.RemoveField(
            model_name='iidrequestor',
            name='username',
        ),
        migrations.AddField(
            model_name='iidrequestor',
            name='requestor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requestor_iid', to='employee.employee'),
            preserve_default=False,
        ),
    ]
