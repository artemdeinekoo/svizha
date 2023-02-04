from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category, Product, Discount, SubCategory, Review



@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    """
    Class for administrating SubCategory model.
    """
    list_display = ("title",)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    """
    Class for administrating Category model.
    """
    list_display = ("title", "slug")


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    """
    Class for administrating Product model.
    """
    list_display = ("category", "image", "price", "grammage", "vendor_code", "title", "description", "recipe",
                    "ingredients", "slug")


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Class for administrating Discount model.
    """
    list_display = ('discount_percentage', 'start_date', 'end_date')


admin.site.register(Review)
