from rest_framework.routers import DefaultRouter
from acc.api.views import TaxViewSet

# Category
router_tax = DefaultRouter()
router_tax.register(prefix='tax', viewset=TaxViewSet, basename='taxes')