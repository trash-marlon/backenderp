# Generated by Django 4.1.4 on 2023-01-05 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0002_configuration_show_blog_configuration_show_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='configuration',
            options={'ordering': ['name'], 'verbose_name': 'Configuration', 'verbose_name_plural': 'Configurations'},
        ),
    ]
