from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Product Name')
    price = models.IntegerField(verbose_name='Product Price')
    description = models.TextField(verbose_name='Product Description')
    stuck = models.IntegerField(verbose_name='Product Stuck')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='Product Registered Date')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
