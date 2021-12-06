from typing import ClassVar
from rest_framework import serializers
from .models import Category, Products, Comments

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsSerializers(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Products
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    # product = ProductsSerializers()
    class Meta:
        model = Comments
        fields = '__all__'