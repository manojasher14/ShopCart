from django.contrib import admin
from .models import category


# Register your models here.
@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'description', 'Cat_image')
    prepopulated_fields = {'slug': ('category_name',)}