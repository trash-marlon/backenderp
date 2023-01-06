# Generated by Django 4.1.4 on 2023-01-06 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0011_country_code'),
        ('pur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='po_company', to='con.contact', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='partner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='po_partner', to='con.contact', verbose_name='Partner'),
        ),
    ]
