from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category, Product, Discount


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("title", "slug")


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("category", "image", "price", "grammage", "vendor_code", "title", "description", "recipe",
                    "ingredients", "slug")


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_percentage', 'start_date', 'end_date')


admin.site.register(Discount, DiscountAdmin)
