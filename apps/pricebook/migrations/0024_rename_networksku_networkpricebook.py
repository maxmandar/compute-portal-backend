# Generated by Django 4.1.7 on 2023-05-09 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricebook', '0023_historicalbigfixpricebook_bigfixpricebook'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NetworkSKU',
            new_name='NetworkPricebook',
        ),
    ]
