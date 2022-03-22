from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SidebarList, SidebarDetail, SidebarViewSet


router = DefaultRouter()
router.register('sidebar', SidebarViewSet)
app_name = "sidebar_api"

urlpatterns = [
    path('<int:pk>/', SidebarDetail.as_view(), name='detailcreate'),
    path('', SidebarList.as_view(), name='listcreate'),
    path('api/',include(router.urls))
]
