# Generated by Django 4.1.4 on 2023-01-06 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0011_country_code'),
        ('sal', '0006_remove_saleorder_company_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorder',
            name='date_confirm',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='seller_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sale_order_seller', to='con.contact', verbose_name='Seller'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='partner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sale_order_partner', to='con.contact', verbose_name='Partner'),
        ),
    ]
