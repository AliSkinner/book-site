from django.contrib import admin
from .models import Author, Book, CarouselSlide

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "surname")}

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CarouselSlideAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(CarouselSlide, CarouselSlideAdmin)
