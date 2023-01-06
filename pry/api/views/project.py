from rest_framework.viewsets import ModelViewSet
from pry.models import Project
from pry.api.serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated

class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()