# Generated by Django 4.1.4 on 2023-01-06 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('con', '0011_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(help_text='Name of project', max_length=100, unique=True)),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('sent', 'Sent'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', max_length=64)),
                ('partner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='con.contact', verbose_name='Partner')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['name'],
            },
        ),
    ]
