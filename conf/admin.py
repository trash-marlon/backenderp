from django.contrib import admin
from .models import Configuration, Cron, Log, Parameter, Note

admin.site.register(Configuration)
admin.site.register(Cron)
admin.site.register(Log)
admin.site.register(Parameter)
admin.site.register(Note)