# Generated by Django 4.1.4 on 2023-01-06 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0011_country_code'),
        ('pur', '0002_purchaseorder_company_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='company_id',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='partner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='con.contact', verbose_name='Partner'),
        ),
    ]