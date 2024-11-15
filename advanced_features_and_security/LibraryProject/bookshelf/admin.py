from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ['title', 'author', 'publication_year']
    search_fields = ['title']

admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ['date_of_birth', 'profile_photo']

admin.site.register(CustomUser, CustomUserAdmin) 