from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("title", "slug")


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("category", "image", "price", "grammage", "vendor_code", "title", "description", "recipe",
                    "ingredients", "slug")
