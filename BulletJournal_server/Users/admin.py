from django.contrib import admin

# Register your models here.
from Users.models import User
'''
admin.site.register(User)
admin.site.register(Roles)
'''

class UserAdmin(admin.ModelAdmin):
    list_display = ("login", "email", "password", "user_id", "role" )

admin.site.register(User, UserAdmin)