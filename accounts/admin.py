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


@admin.register(CustomUser)
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
        (None, {'fields': ('username', 'email', 'password')}),
        ('Account Tier', {'fields': ('account_tier',)}),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active',
                'is_superuser',
                'user_permissions')
                }
        ),
        ('Additional stats', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Username', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_staff',)}),
        ('Account Tier', {'fields': ('account_tier',)}),
    )


@admin.register(AccountTier)
class AccountTierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'thumbnail_size_for_admin_site',
        'is_expiring_link',
        'is_original_file'
    )
