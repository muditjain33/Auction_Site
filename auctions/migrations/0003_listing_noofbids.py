# Generated by Django 3.0.8 on 2020-07-19 11:20

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_wishlistby'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='noofbids',
            field=models.IntegerField(blank=True, default=0, verbose_name=auctions.models.User),
        ),
    ]
