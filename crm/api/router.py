from rest_framework.routers import DefaultRouter
from crm.api.views import LeadViewSet

# Course
router_lead = DefaultRouter()
router_lead.register(prefix='lead', viewset=LeadViewSet, basename='leads')