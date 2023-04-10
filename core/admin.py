from django.contrib import admin

from core.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass
