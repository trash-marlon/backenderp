from rest_framework.routers import DefaultRouter
from conf.api.views import ConfigurationViewSet, CronViewSet, LogViewSet

# Configuration
router_configuration = DefaultRouter()
router_configuration.register(prefix='configuration', viewset=ConfigurationViewSet, basename='configurations')


# Cron
router_cron = DefaultRouter()
router_cron.register(prefix='cron', viewset=CronViewSet, basename='crons')

# Log
router_log = DefaultRouter()
router_log.register(prefix='log', viewset=LogViewSet, basename='logs')