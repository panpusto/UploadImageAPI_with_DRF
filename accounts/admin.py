from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
    AccountTier
)
from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm
)


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'account_tier'
    )
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Username', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff',)}),
        ('Account Tier', {'fields': ('account_tier',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Username', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff',)}),
        ('Account Tier', {'fields': ('account_tier',)}),
    )


class AccountTierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'thumbnail_size_for_admin_site',
        'is_expiring_link',
        'is_original_file'
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AccountTier, AccountTierAdmin)
