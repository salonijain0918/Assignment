from django.urls import path
from .views import ListCategories, ListSubcategories, ListProducts
urlpatterns = [
    path('categories', ListCategories.as_view(), name='Categories'),
    path('subcategories', ListSubcategories.as_view(), name='Subcategories'),
    path('products', ListProducts.as_view(), name='Products'),
]
