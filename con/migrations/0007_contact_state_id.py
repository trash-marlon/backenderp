# Generated by Django 4.1.4 on 2023-01-04 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('con', '0006_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='state_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='con.state', verbose_name='State'),
        ),
    ]
