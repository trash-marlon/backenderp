
from rest_framework.routers import DefaultRouter
from pry.api.views import ProjectViewSet

# Category
router_project = DefaultRouter()
router_project.register(prefix='project', viewset=ProjectViewSet, basename='project')