# Generated by Django 4.1.4 on 2023-01-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0007_contact_state_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='own_company',
            field=models.BooleanField(default=False),
        ),
    ]