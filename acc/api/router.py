from rest_framework.routers import DefaultRouter
from acc.api.views import TaxViewSet, CurrencyViewSet

# Tax
router_tax = DefaultRouter()
router_tax.register(prefix='tax', viewset=TaxViewSet, basename='taxes')

# Currency
router_currency = DefaultRouter()
router_currency.register(prefix='currency', viewset=CurrencyViewSet, basename='currency')