# Generated by Django 4.1.4 on 2023-01-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0002_alter_contact_city_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='customer_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='supplier_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
