from django.contrib import admin
from .models import Configuration, Cron

admin.site.register(Configuration)
admin.site.register(Cron)