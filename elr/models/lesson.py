from django.db import models
from base.models import ClassModel
from elr.models.course import Course
from django.utils import timezone

class Lesson(ClassModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    course_id = models.ForeignKey(
        Course,
        related_name='course_lesson',
        on_delete=models.PROTECT,
        verbose_name='Course',
        null=True,
        blank=True
    )

    video_link = models.CharField(max_length=255, blank=True, null=True)

    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'lesson'