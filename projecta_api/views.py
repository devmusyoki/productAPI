from rest_framework import generics
from projecta.models import Product
from .serializers import ProductSerializer

class ProductList(generic.ListCreateAPIView):
    queryset = Product.productobjects.all()
    serializer_class = ProductSerializer
    pass

class ProductDetail(generics.RetrieveDestroyAPIView):
    pass
