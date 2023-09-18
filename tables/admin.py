from django.contrib import admin
from .models import Table, Item

# Register your models here.


class TableAdmin(admin.ModelAdmin):
    """Table Admin model"""
    model = Table
    filter_horizontal = ('items',)


admin.site.register(Table, TableAdmin)
admin.site.register(Item)
