from rest_framework.routers import DefaultRouter
from elr.api.views import CourseViewSet

# Course
router_course = DefaultRouter()
router_course.register(prefix='course', viewset=CourseViewSet, basename='courses')