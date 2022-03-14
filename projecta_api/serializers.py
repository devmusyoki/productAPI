from rest_framework import serializers
from projecta.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'link','price',)
