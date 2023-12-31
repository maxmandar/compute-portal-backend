# Generated by Django 4.1.7 on 2023-04-10 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricebook', '0007_pricebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='networksku',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pricebook',
            name='server_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='pricebook.servertype'),
            preserve_default=False,
        ),
    ]
