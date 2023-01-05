from django.db import models
from base.models import ClassModel

class Country(ClassModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']