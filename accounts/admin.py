from django.contrib import admin
from .models import Staff
# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    """Staff Admin model"""
    model = Staff
    filter_horizontal = ('workplaces',)


admin.site.register(Staff, StaffAdmin)
