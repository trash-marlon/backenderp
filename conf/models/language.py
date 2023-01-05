from django.db import models
from base.models import ClassModel

class Language(ClassModel):
    name = models.CharField('Name', max_length=40)

    class Meta:
        ordering = ['-fc']

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"