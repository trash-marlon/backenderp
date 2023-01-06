
from rest_framework.routers import DefaultRouter
from pry.api.views import ProjectViewSet, TaskViewSet

# Project
router_project = DefaultRouter()
router_project.register(prefix='project', viewset=ProjectViewSet, basename='project')

# Task
router_task = DefaultRouter()
router_task.register(prefix='task', viewset=TaskViewSet, basename='task')