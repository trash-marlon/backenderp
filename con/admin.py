from django.contrib import admin

from .models import Contact, Country

# Register your models here.
admin.site.register(Contact)
admin.site.register(Country)