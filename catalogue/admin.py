from django.contrib import admin
from .models import Author, Book, CarouselSlide, MailingListSubscriber

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "surname")}
    list_display = ('get_fullname', 'nationality', 'date_of_birth', 'date_of_death', 'number_of_books', 'slug')

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'pub_date', 'isbn', 'slug',)

class CarouselSlideAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display = ('title', 'url', 'active','created_on',)


class MailingListSubscriberAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display = ('email', 'seen', 'created_on')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(CarouselSlide, CarouselSlideAdmin)
admin.site.register(MailingListSubscriber, MailingListSubscriberAdmin)
