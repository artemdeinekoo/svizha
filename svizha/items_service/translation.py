from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, SubCategory


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'recipe', 'ingredients')
