from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
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

    def __str__(self):
        return self.title

