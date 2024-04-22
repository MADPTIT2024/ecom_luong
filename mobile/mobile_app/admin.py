from django.contrib import admin

# Register your models here.
from .models import Mobile, Category


admin.site.register(Mobile)
admin.site.register(Category)
