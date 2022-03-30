from rest_framework import serializers
from projecta.models import Category
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'type', 'children')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['children'] = CategorySerializer(many=True)
        return fields


