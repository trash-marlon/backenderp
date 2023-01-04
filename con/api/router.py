from rest_framework.routers import DefaultRouter
from con.api.views import ContactViewSet, CountryViewSet, StateViewSet

# Contact
router_contact = DefaultRouter()
router_contact.register(prefix='contact', viewset=ContactViewSet, basename='contact')

# Country
router_country = DefaultRouter()
router_country.register(prefix='country', viewset=CountryViewSet, basename='country')

# State
router_state = DefaultRouter()
router_state.register(prefix='state', viewset=StateViewSet, basename='state')