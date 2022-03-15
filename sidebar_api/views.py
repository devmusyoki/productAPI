from rest_framework import generics
from projecta.models import Category
from .serializers import CategorySerializer

class CategoryList(generics.ListCreateAPIView):
    querysert = Category.objects.all()
    serializer_class = CategorySerializer
    pass

class CategoryDetail(generics.RetrieveDestroyAPIView):
    querysert = Category.objects.all()
    serializer_class = CategorySerializer
    pass
