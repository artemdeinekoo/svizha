from rest_framework import serializers
from .models import Product, Category, Discount, Review


class DiscountSerializer(serializers.ModelSerializer):
    """
    Serializer that provides the info about discount.
    """

    class Meta:
        model = Discount
        fields = ('discount_percentage', 'start_date', 'end_date')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category
    """

    class Meta:
        model = Category
        fields = ('id', 'title', 'subcategory', 'image', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product
    """
    discount = DiscountSerializer()
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'category', 'image', 'price', 'grammage', 'vendor_code', 'title', 'description', 'recipe',
            'ingredients',
            'slug', 'discount', 'discounted_price')

    def get_discounted_price(self, obj):
        """
        Method to add discount info for json
        """
        return int(obj.apply_discount())


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product_id', 'user_id', 'rating', 'text')
