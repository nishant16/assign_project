from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Subcategory
from .models import Product


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)

