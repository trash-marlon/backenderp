from rest_framework.routers import DefaultRouter
from con.api.views import ContactViewSet

router_contact = DefaultRouter()

router_contact.register(prefix='contact', viewset=ContactViewSet, basename='contact')