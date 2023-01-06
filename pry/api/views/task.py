from rest_framework.viewsets import ModelViewSet
from pry.models import Task
from pry.api.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()