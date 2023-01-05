from django.db import models
from base.models import ClassModel

class Log(ClassModel):
    name = models.CharField('Name', max_length=40)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"