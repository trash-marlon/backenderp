from django.db import models
from base.models import ClassModel

class Note(ClassModel):
    name = models.CharField('Name', max_length=40)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fc']

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"