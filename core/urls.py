from core import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),                    # Django admin route
    path("consultas/", include("apps.operaciones.apis.urls")),
    path("", include("apps.authentication.urls")),      # Auth routes - login / register
    path("", include("apps.home.urls")),                # UI Kits Html files
]

#if not settings.DEBUG:
handler403 = 'apps.home.views.permission_denied'