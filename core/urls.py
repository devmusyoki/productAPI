from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("sidebar_api.urls", namespace="sidebar_api")),
    path('api/', include("projecta_api.urls", namespace="products_api")),
]
