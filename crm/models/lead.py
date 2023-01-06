from django.db import models
from base.models import ClassModel
from django.utils import timezone

class Lead(ClassModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lead'