from django.urls import path
from .views import SidebarList, SidebarDetail

app_name = "sidebar_api"

urlpatterns = [
    path('<int:pk>/', SidebarDetail.as_view(), name='detailcreate'),
    path('', SidebarList.as_view(), name='listcreate'),
]
