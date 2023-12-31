from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    """
    User account admin
    """

    list_display = ('nickname', 'email')
    readonly_fields = ('id', 'date_joined', 'last_login')
    prepopulated_fields = {'slug': ('nickname', )}
    fieldsets = (
        (None, {
            'fields': ('id', 'nickname', 'email', 'img', 'slug', 'is_admin', 'is_active',
                       'is_staff', 'is_superuser', 'date_joined', 'last_login'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nickname', 'email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    ordering = ()
    list_filter = ()
