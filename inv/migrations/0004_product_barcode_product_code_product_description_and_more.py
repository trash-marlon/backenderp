# Generated by Django 4.1.4 on 2023-01-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0003_uom'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, help_text='Barcode of Product', max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, help_text='Code of Product', max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Description of Product', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='for_purchase',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='for_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('service', 'Service'), ('product', 'Product'), ('cons', 'Consumable')], default='product', max_length=100),
        ),
    ]
