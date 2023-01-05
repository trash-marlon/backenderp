from django.contrib import admin
from .models import Contact, Country, State

# Register your models here.
admin.site.register(Contact)
admin.site.register(Country)
admin.site.register(State)
