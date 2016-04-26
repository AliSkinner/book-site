from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "surname")}

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
