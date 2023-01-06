from rest_framework.routers import DefaultRouter
from sal.api.views import SaleOrderViewSet, SaleOrderLineViewSet

# SaleOrder
router_saleorder = DefaultRouter()
router_saleorder.register(prefix='saleorder', viewset=SaleOrderViewSet, basename='saleorders')


# SaleOrderLine
router_saleorderline = DefaultRouter()
router_saleorderline.register(prefix='saleorderline', viewset=SaleOrderLineViewSet, basename='saleorderlines')