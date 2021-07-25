from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Categories, Subcategories, Product
from .serializers import CategoriesSerializer, SubcategoriesSerializer, ProductSerializer


class ListCategories(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ListSubcategories(APIView):
    def get(self, request):
        subcategories = Subcategories.objects.all()
        serializer = SubcategoriesSerializer(subcategories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubcategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ListProducts(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
