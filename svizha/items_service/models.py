from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from authentication.models import User


class Discount(models.Model):
    """
    Class that represents discount system on the website.
    """
    discount_percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.discount_percentage)


class SubCategory(models.Model):
    """
    Class that makes it possible to make subcategory for each category.
    """
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    Class that represents category system on the website.
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='categories')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcategory')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Class that represents product on the website.
    """
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='products')
    price = models.IntegerField()
    grammage = models.IntegerField()
    vendor_code = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    recipe = models.TextField()
    ingredients = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def apply_discount(self):
        """
        Method that allows to use discounts.
        """
        if self.discount and self.discount.start_date <= timezone.now() <= self.discount.end_date:
            discount_percentage = self.discount.discount_percentage
            return self.price - (self.price * discount_percentage / 100)
        return self.price

    def __str__(self):
        return self.title


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
