from django.db import models
from base.models import ClassModel


CRON_CHOICE = (
    ("minutes", "Minutes"),
    ('hours', 'Hours'),
    ('day', 'Day'),
    ('work_day', 'Work Day'),
    ('weeks', 'Weeks'),
    ('month', 'Month'),
)

class Cron(ClassModel):
    name = models.CharField('Name', max_length=40)
    interval_type = models.CharField(
        choices=CRON_CHOICE, max_length=64, default='hours')
    model_name = models.CharField('Model', max_length=40)
    function = models.CharField('Function', max_length=40)
    number_call = models.IntegerField('Numer of calls', default=-1)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cron'
        verbose_name_plural = 'Crons'
        ordering = ['name']