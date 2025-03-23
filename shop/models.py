from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.TextField(blank = True)
    cat_image = models.ImageField(upload_to = 'photo/categories/', blank = True)
    # date_created = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'photo/products')
    stock = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)

    is_available = models.BooleanField(default = True)

    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.product_name