from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projecta.urls", namespace="products")),
    path('api/', include("projecta_api.urls", namespace="products_api"))
]
