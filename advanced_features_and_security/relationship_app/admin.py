from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import UserProfile

# Register your models here.
class ModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ['date_of_birth', 'profile_photo']

admin.site.register(ModelAdmin, User)    