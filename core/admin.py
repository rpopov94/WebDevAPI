from django.contrib import admin

from core.models import CustomUser, Post

admin.site.register(Post)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass
