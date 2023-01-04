# Generated by Django 4.1.4 on 2023-01-04 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0004_product_barcode_product_code_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='inv.category', verbose_name='Category'),
        ),
    ]
