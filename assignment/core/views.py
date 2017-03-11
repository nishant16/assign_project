from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from .serializers import CategoryModelSerializer ,SubcategoryModelSerializer,\
                        ProductModelSerializer, CreateProductModelSerializer
from .models import Category ,Subcategory, Product


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class SubcategoryListAPIView(generics.ListAPIView):
    serializer_class= SubcategoryModelSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Subcategory.objects.filter(category__name= category_name)


# class ProductListAPIView(generics.ListAPIView):
#     serializer_class= ProductModelSerializer
#     def get_queryset(self):
#         subcategory_name = self.kwargs['subcategory_name']
#         return Product.objects.filter(subcategory__name=subcategory_name)
#

class ProductListAPIView(generics.ListAPIView):
    serializer_class= ProductModelSerializer

    def get_queryset(self):
        qs=Product.objects.all().select_related('subcategory')
        subcategory_query=self.request.GET.get("subcategory",None)
        category_query=self.request.GET.get("category",None)
        if subcategory_query is not None:
            qs = qs.filter(subcategory__name=subcategory_query)
        elif category_query is not None:
            qs = qs.filter(subcategory__category__name=category_query)
        else:
            qs = qs
        return qs


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductModelSerializer