# Generated by Django 4.1.4 on 2023-01-06 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0011_country_code'),
        ('sal', '0003_alter_saleorder_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorder',
            name='company_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='company', to='con.contact', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='partner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='partner', to='con.contact', verbose_name='Partner'),
        ),
    ]
