from rest_framework.routers import DefaultRouter
from inv.api.views import CategoryViewSet, ProductViewSet, UomViewSet, WarehouseViewSet, LocationViewSet, BrandViewSet, ModelViewSet

# Category
router_category = DefaultRouter()
router_category.register(prefix='category', viewset=CategoryViewSet, basename='categories')

# Product
router_product = DefaultRouter()
router_product.register(prefix='product', viewset=ProductViewSet, basename='products')

# Uom
router_uom = DefaultRouter()
router_uom.register(prefix='uom', viewset=UomViewSet, basename='uoms')

# Warehouse
router_warehouse = DefaultRouter()
router_warehouse.register(prefix='warehouse', viewset=WarehouseViewSet, basename='warehouses')

# Location
router_location = DefaultRouter()
router_location.register(prefix='location', viewset=LocationViewSet, basename='locations')

# Brand
router_brand = DefaultRouter()
router_brand.register(prefix='brand', viewset=BrandViewSet, basename='brands')

# Model
router_model = DefaultRouter()
router_model.register(prefix='model', viewset=ModelViewSet, basename='models')