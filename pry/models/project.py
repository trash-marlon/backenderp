from django.db import models
from base.models import ClassModel
from con.models.contact import Contact


STATE = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    )


class Project(ClassModel):
    name = models.CharField(max_length=100, 
    unique=True,
    help_text='Name of project')

    partner_id = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        verbose_name=('Partner'),
        null=True,
        blank=True
    )

    state = models.CharField(
        choices=STATE, max_length=64, default='draft')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['name']