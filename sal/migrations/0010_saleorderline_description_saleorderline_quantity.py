# Generated by Django 4.1.4 on 2023-01-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sal', '0009_saleorderline'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorderline',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='saleorderline',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Quantity'),
        ),
    ]
