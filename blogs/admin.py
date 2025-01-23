from django.contrib import admin
from .models import Blog

# Register your models here.
admin.site.register(Blog)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'date_created')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'date_created')
