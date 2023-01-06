from django.db import models
from base.models import ClassModel
from con.models.contact import Contact
from pry.models.project import Project

STATE = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    )

class Task(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name')

    partner_id = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        verbose_name=('Partner'),
        null=True,
        blank=True
    )

    project_id = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        verbose_name=('Project'),
        null=True,
        blank=True
    )

    state = models.CharField(
        choices=STATE, max_length=64, default='draft')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['name']