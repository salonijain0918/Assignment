from rest_framework import serializers
from .models import Categories, Subcategories, Product


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Categories


class SubcategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Subcategories


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name')
        model = Product
