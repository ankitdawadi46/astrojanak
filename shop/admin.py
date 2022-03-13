from django.contrib import admin
from .models import products, product_categories,orders
class productsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('subcategory',)}
class product_categoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
# Register your models here.
admin.site.register(products,productsAdmin)
admin.site.register(product_categories,product_categoriesAdmin)
admin.site.register(orders)
