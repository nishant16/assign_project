from rest_framework import serializers

from .models import Category, Subcategory, Product


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=[
            'name'
        ]


class SubcategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subcategory
        fields=[
             'name'
         ]


class ProductModelSerializer(serializers.ModelSerializer):
    subcategory = SubcategoryModelSerializer()
    class Meta:
        model= Product
        fields=[
            'name','subcategory'
         ]

class CreateProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=[
            'name','subcategory'
         ]