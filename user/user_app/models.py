from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=20)
    role = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.email