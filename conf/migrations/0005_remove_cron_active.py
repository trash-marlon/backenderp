# Generated by Django 4.1.4 on 2023-01-05 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0004_cron'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cron',
            name='active',
        ),
    ]
