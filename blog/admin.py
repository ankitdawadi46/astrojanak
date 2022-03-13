from django.contrib import admin
from .models import blogs

class blogsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # new
# Register your models here.
admin.site.register(blogs, blogsAdmin)
