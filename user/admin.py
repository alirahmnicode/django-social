from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "phone_number", "is_staff", "is_active_account")

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
