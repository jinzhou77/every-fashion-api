# Generated by Django 3.2.4 on 2021-07-29 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0014_ebaytrades_ebay_trade_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='average_sale_price',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='number_of_sale',
        ),
    ]
