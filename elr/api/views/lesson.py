from rest_framework.viewsets import ModelViewSet
from elr.models import Lesson
from elr.api.serializers import LessonSerializer
from rest_framework.permissions import IsAuthenticated

class LessonViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()