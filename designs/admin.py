from django.contrib import admin

# Register your models here.
from designs.models import Designs


class DesignAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_area', 'name', 'price', 'created_by')
    list_filter = ('created_by', 'price', 'total_area')
    inlines = (

    )


admin.site.register(Designs, DesignAdmin)
