from rest_framework.routers import DefaultRouter
from sal.api.views import SaleOrderViewSet

# Category
router_saleorder = DefaultRouter()
router_saleorder.register(prefix='saleorder', viewset=SaleOrderViewSet, basename='saleorders')