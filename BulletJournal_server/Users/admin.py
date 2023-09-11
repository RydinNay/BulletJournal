from django.contrib import admin
from Users.models import User, Role


class UserAdmin(admin.ModelAdmin):
    list_display = ("login", "email", "password", "user_id", "role" )


class RoleAdmin(admin.ModelAdmin):
    list_display = ("role_id", "role_name", "description")


admin.site.register(User, UserAdmin)
admin.site.register(Role, RoleAdmin)
