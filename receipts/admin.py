from django.contrib import admin
from .models import Receipt, Item

# Register your models here.


class ReceiptAdmin(admin.ModelAdmin):
    """Receipt Admin model"""
    model = Receipt
    filter_horizontal = ('items',)


admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Item)
