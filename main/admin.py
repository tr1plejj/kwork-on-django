from django.contrib import admin
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username__startswith',)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('author',)
