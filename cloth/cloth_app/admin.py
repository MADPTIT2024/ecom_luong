from django.contrib import admin

# Register your models here.
from .models import Cloth, Category


admin.site.register(Cloth)
admin.site.register(Category)
