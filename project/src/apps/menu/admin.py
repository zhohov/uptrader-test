from django.contrib import admin

from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    ...


class MenuItemAdmin(admin.ModelAdmin):
    ...


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
