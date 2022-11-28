from django.contrib import admin

from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    list_dilter = ['name', 'price']
