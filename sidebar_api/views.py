from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from projecta.models import Category
from .serializers import CategorySerializer
from rest_framework import generics

class SidebarList(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent', 'title', 'description' ]
    pass


class SidebarDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    pass

class SidebarViewSet (ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent=None)
