from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_name', 'last_login','date_joined', 'is_admin', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'user_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('user_name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

