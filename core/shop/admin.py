from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
  #list_display = ('name', 'image', 'description')
  readonly_fields = ('id',)

class ProductAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor)  
