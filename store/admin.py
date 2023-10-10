from django.contrib import admin

# Register your models here.
from . models import *

# admin.site.register(Category)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
