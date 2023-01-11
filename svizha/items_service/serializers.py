from rest_framework import serializers
from .models import Product, Category, Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ('discount_percentage', 'start_date', 'end_date')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer()
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'image', 'price', 'grammage', 'vendor_code', 'title', 'description', 'recipe',
            'ingredients',
            'slug', 'discount', 'discounted_price')

    def get_discounted_price(self, obj):
        return int(obj.apply_discount())
