from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser


class BlogUserAdmin(UserAdmin):
    
    # fields to display
    list_display = ('username', 'email', 'phone_number', 'date_of_birth', 'is_staff' )
    # fields to include in the add/edit user forms 
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # fields to include in the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'date_of_birth', 'profile_picture'),
        }),
    )










# Register your models here.
admin.site.register(BlogUser, BlogUserAdmin)

