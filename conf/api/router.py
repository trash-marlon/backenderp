from rest_framework.routers import DefaultRouter
from conf.api.views import ConfigurationViewSet, CronViewSet, LogViewSet, ParameterViewSet, NoteViewSet

# Configuration
router_configuration = DefaultRouter()
router_configuration.register(prefix='configuration', viewset=ConfigurationViewSet, basename='configurations')


# Cron
router_cron = DefaultRouter()
router_cron.register(prefix='cron', viewset=CronViewSet, basename='crons')

# Log
router_log = DefaultRouter()
router_log.register(prefix='log', viewset=LogViewSet, basename='logs')

# Parameter
router_parameter = DefaultRouter()
router_parameter.register(prefix='parameter', viewset=ParameterViewSet, basename='parameters')

# Note
router_note = DefaultRouter()
router_note.register(prefix='note', viewset=NoteViewSet, basename='notes')