from django.db import models
from django.utils import timezone


class Discount(models.Model):
    discount_percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.discount_percentage)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
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
        if self.discount and self.discount.start_date <= timezone.now() <= self.discount.end_date:
            discount_percentage = self.discount.discount_percentage
            return self.price - (self.price * discount_percentage / 100)
        return self.price

    def __str__(self):
        return self.title
