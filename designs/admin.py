from django.contrib import admin

# Register your models here.
from designs.models import Designs, Post


class DesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_area', 'name', 'price', 'created_by')
    list_filter = ('created_by', 'price', 'total_area')


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'design', 'created_on', 'email')
    list_filter = ('design', 'created_on')
    search_fields = ('name', 'email', 'text')


admin.site.register(Designs, DesignAdmin)
admin.site.register(Post, PostAdmin)
