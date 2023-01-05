"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# inv
from inv.api.router import router_category, router_product, router_uom


# web
from web.api.router import router_post

# con
from con.api.router import router_contact, router_state, router_country

# sal
from sal.api.router import router_saleorder

# pur
from pur.api.router import router_purchaseorder

schema_view = get_schema_view(
   openapi.Info(
      title="BackendERP API",
      default_version='v1',
      description="Documentation for BackendERP API",
      terms_of_service="",
      contact=openapi.Contact(email="mfalconsoft@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', include(('www.urls', 'www'), namespace='www')),
    path('admin/', admin.site.urls),

    # Swagger
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # API
    path('api/', include(('users.api.router', 'users'), namespace='users')),

    # con
    path('api/', include(router_contact.urls)),
    path('api/', include(router_country.urls)),
    path('api/', include(router_state.urls)),

     # inv
    path('api/', include(router_category.urls)),
    path('api/', include(router_product.urls)),
    path('api/', include(router_uom.urls)),
    
    # www
    path('api/', include(router_post.urls)),

    # sal
    path('api/', include(router_saleorder.urls)),

    # pur
    path('api/', include(router_purchaseorder.urls)),
]
