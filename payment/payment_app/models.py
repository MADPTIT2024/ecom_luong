from django.db import models
from django.utils import timezone

# Create your models here.
class Payment(models.Model):
    user_id = models.IntegerField(null=True, default=None)
    amount = models.FloatField(null=True, default=0)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return str(self.id)