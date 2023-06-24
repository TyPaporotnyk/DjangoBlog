from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    """
    User account admin
    """
    list_display = ('nickname', 'email')

    readonly_fields = ('id', 'date_joined', 'last_login') 
    
    fieldsets = (
        (None, {
            'fields': ('id', 'nickname', 'email', 'img', 'date_joined', 'last_login')
        }),
    ) 

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            'fields': ('nickname', 'email', 'password1', 'password2')
        }),
    ) 

    filter_horizontal = ()
    ordering = ()
    list_filter = ()