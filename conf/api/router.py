from rest_framework.routers import DefaultRouter
from conf.api.views import ConfigurationViewSet

# Category
router_configuration = DefaultRouter()
router_configuration.register(prefix='configuration', viewset=ConfigurationViewSet, basename='configurations')