# Generated by Django 2.0.5 on 2018-06-06 04:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0002_auto_20180606_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcescrapeyellowpages',
            name='street_address',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='sourcescrapeyellowpages',
            table='_source_scrape_yellowpages',
        ),
    ]
