from rest_framework.routers import DefaultRouter
from elr.api.views import CourseViewSet, LessonViewSet

# Course
router_course = DefaultRouter()
router_course.register(prefix='course', viewset=CourseViewSet, basename='courses')

# Lesson
router_lesson = DefaultRouter()
router_lesson.register(prefix='lesson', viewset=LessonViewSet, basename='lessons')