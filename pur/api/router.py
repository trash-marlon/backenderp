from rest_framework.routers import DefaultRouter
from pur.api.views import PurchaseOrderViewSet

# Category
router_purchaseorder = DefaultRouter()
router_purchaseorder.register(prefix='purchaseorder', viewset=PurchaseOrderViewSet, basename='purchaseorders')