from rest_framework.routers import DefaultRouter
from acc.api.views import TaxViewSet, CurrencyViewSet, JournalViewSet

# Tax
router_tax = DefaultRouter()
router_tax.register(prefix='tax', viewset=TaxViewSet, basename='taxes')

# Currency
router_currency = DefaultRouter()
router_currency.register(prefix='currency', viewset=CurrencyViewSet, basename='currency')

# Journal
router_journal = DefaultRouter()
router_journal.register(prefix='journal', viewset=JournalViewSet, basename='journals')