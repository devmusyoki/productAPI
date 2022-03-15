from rest_framework import serializers
from projecta.models import Category

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('title',) 