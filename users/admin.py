from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('profession',)
    search_fields = ('username__startswith', 'first_name', 'last_name')
    fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'gender',
              'about', 'telegram', 'vk', 'exp', 'profession', 'avatar')
