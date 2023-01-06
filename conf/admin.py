from django.contrib import admin
from .models import Configuration, Cron, Log, Parameter, Note, Language, Sequence

admin.site.register(Configuration)
admin.site.register(Cron)
admin.site.register(Log)
admin.site.register(Parameter)
admin.site.register(Note)
admin.site.register(Language)
admin.site.register(Sequence)