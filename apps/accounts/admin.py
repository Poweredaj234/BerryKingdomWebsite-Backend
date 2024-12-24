from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nobility', 'house', 'balance')
    search_fields = ('username', 'email')
    list_filter = ('nobility', 'house')
