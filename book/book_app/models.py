from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)	

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)	
    address = models.CharField(max_length=100)	
    email = models.CharField(max_length=100)	


class Publisher(models.Model):
    name = models.CharField(max_length=100)	
    address = models.CharField(max_length=100)	
    email = models.CharField(max_length=100)	

class Book(models.Model):
    title = models.CharField(max_length=100)	
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, default=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True, default=None)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,null=True, default=None)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.CharField(max_length=500,null=True)

    is_sale = models.BooleanField(default=False,null=True)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6,null=True)

    def __str__(self):
        return self.title


