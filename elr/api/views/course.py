from rest_framework.viewsets import ModelViewSet
from elr.models import Course
from elr.api.serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated

class CourseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()