from rest_framework.routers import DefaultRouter
from inv.api.views import CategoryViewSet, ProductViewSet

# Category
router_category = DefaultRouter()
router_category.register(prefix='category', viewset=CategoryViewSet, basename='categories')

# Product
router_product = DefaultRouter()
router_product.register(prefix='product', viewset=ProductViewSet, basename='products')