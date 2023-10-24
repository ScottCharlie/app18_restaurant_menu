from django.contrib import admin
from .models import Item

# Defines how the admin userface will look like
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status", )
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)
