# Generated by Django 4.1.7 on 2023-03-05 11:01

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('infrastructureinitiationdocument', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iidproject',
            name='fsm_state',
            field=django_fsm.FSMField(choices=[('Draft', 'Draft'), ('Review', 'Review'), ('Submitted', 'Submitted'), ('Verified', 'Verified'), ('Approved', 'Approved'), ('Cancelled', 'Cancelled'), ('Rework', 'Rework'), ('Resubmitted', 'Resubmitted'), ('Rereviewed', 'Rereviewed')], default='Draft', max_length=50, protected=True),
        ),
    ]