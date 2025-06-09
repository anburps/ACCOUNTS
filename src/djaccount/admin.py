from django.contrib import admin

# Register your models here.
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomeUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active','is_superuser','date_joined','last_login')
    ordering = ('-date_joined',)
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    

admin.site.register(CustomUser,CustomeUserAdmin)