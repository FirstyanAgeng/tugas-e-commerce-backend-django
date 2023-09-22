from django.contrib import admin
from .models import User, Product, Order, OrderItem
# Register your models here.
from django.contrib import admin
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('name','email', 'password', 'role')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'email',
                'password1',
                'password2',
                'role',
                'phone_number',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)