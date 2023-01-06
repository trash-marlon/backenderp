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
from inv.api.router import router_category, router_product, router_uom, router_warehouse, router_location, router_brand


# web
from web.api.router import router_post

# con
from con.api.router import router_contact, router_state, router_country

# sal
from sal.api.router import router_saleorder, router_saleorderline

# pur
from pur.api.router import router_purchaseorder

# conf
from conf.api.router import router_configuration, router_cron, router_log, router_parameter, router_note, router_language, router_sequence

# acc
from acc.api.router import router_tax, router_currency, router_journal

# elr
from elr.api.router import router_course, router_lesson

# pry
from pry.api.router import router_project, router_task


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
    path('api/', include(router_warehouse.urls)),
    path('api/', include(router_location.urls)),
    path('api/', include(router_brand.urls)),

    # www
    path('api/', include(router_post.urls)),

    # sal
    path('api/', include(router_saleorder.urls)),
    path('api/', include(router_saleorderline.urls)),

    # pur
    path('api/', include(router_purchaseorder.urls)),

    # conf
    path('api/', include(router_configuration.urls)),
    path('api/', include(router_cron.urls)),
    path('api/', include(router_log.urls)),
    path('api/', include(router_parameter.urls)),
    path('api/', include(router_note.urls)),
    path('api/', include(router_language.urls)),
    path('api/', include(router_sequence.urls)),

    # acc
    path('api/', include(router_tax.urls)),
    path('api/', include(router_currency.urls)),
    path('api/', include(router_journal.urls)),

    # elr
    path('api/', include(router_course.urls)),
    path('api/', include(router_lesson.urls)),

    # pry
    path('api/', include(router_project.urls)),
    path('api/', include(router_task.urls)),

]
