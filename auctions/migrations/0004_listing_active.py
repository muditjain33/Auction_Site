# Generated by Django 3.0.8 on 2020-07-19 11:50

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_noofbids'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(blank=True, default=0, verbose_name=auctions.models.User),
        ),
    ]
