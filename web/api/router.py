from rest_framework.routers import DefaultRouter
from web.api.views import PostViewSet

router_post = DefaultRouter()

router_post.register(prefix='posts', viewset=PostViewSet, basename='posts')