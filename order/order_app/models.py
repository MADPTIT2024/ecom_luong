from django.db import models
from django.utils import timezone

class Order(models.Model):
    user_id = models.IntegerField(null=True, default=None)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    shipment_id = models.IntegerField(null=True, default=None)
    payment_id = models.IntegerField(null=True, default=None)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product_id = models.IntegerField(null=True, default=None)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    type_product = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)







