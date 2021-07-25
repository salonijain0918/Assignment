from django.contrib import admin
from .models import Categories, Subcategories, Product


# Register your models here.
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subcategory']

