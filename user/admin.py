from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "phone_number", "is_staff", "is_active_account")

admin.site.register(User, CustomUserAdmin)