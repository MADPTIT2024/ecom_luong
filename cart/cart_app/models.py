from django.db import models
import datetime
from django.utils import timezone

class Cart(models.Model):
    user_id = models.IntegerField(null=True, default=None)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_id



class CartProduct(models.Model):
    product_id = models.IntegerField(null=True, default=None)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    type_product = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.quantity} of {self.type_product} : {self.product_id}"




