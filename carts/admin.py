from django.contrib import admin
from .models import Cart, Cartitem

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Cartitem)
class CartitemAdmin(admin.ModelAdmin):
    pass