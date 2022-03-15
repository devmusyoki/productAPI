from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from projecta.models import Category


class CategorySerializer(serializers.ModelSerializer):
    subCategories = serializers.ListSerializer(
        source="subcategories", required=False, child=RecursiveField(), read_only=True)

    class Meta:
        model = Category
        fields = ['title', 'subcategories']

