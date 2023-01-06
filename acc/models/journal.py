from django.db import models
from base.models import ClassModel

TYPE = (
    ("bank", "bank"),
    ('cash', 'cash'),
    ('credit', 'credit'),
    ('debit', 'debit'),
    ('other', 'other'),
)


class Journal(ClassModel):
    name = models.CharField('Name', max_length=40)
    _type = models.CharField(
        choices=TYPE, max_length=64, default='after')


    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journals"