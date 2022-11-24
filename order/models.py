from django.db import models


class Order(models.Model):
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='Buy User Id')
    product_id = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Product Id')
    quantity = models.IntegerField(verbose_name="Product Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Order Data CrateDate')

    def __str__(self):
        return f'{self.user_id}_{self.product_id}'

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

