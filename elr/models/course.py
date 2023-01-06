from django.db import models
from base.models import ClassModel
from con.models.contact import Contact
from django.utils import timezone

class Course(ClassModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    partner_id = models.ForeignKey(
        Contact,
        related_name='course_partner',
        on_delete=models.PROTECT,
        verbose_name='Partner',
        null=True,
        blank=True
    )

    teacher_id = models.ForeignKey(
        Contact,
        related_name='course_teacher',
        on_delete=models.PROTECT,
        verbose_name='Teacher',
        null=True,
        blank=True
    )





    def __str__(self):
        return self.name

    class Meta:
        db_table = 'course'