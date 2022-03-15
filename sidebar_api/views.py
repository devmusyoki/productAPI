from rest_framework import generics
from projecta.models import Category
from .serializers import CategorySerializer

class SidebarList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pass

class SidebarDetail(generics.RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pass
