from typing import ClassVar
from rest_framework import serializers
from .models import Category, Products

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Products
        fields = '__all__'
