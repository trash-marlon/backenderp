# Generated by Django 4.1.4 on 2023-01-06 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sal', '0007_saleorder_date_confirm_saleorder_note_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleorder',
            options={'ordering': ['pk'], 'verbose_name': 'Sale Order', 'verbose_name_plural': 'Sale Orders'},
        ),
        migrations.AddField(
            model_name='saleorder',
            name='date_order',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
