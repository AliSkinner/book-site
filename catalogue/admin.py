from django.contrib import admin
from .models import Author, Book, CarouselSlide, MailingListSubscriber
import csv
from django.http import HttpResponse
from django.utils import timezone

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("first_name", "surname")}
    list_display = ('get_fullname', 'nationality', 'date_of_birth', 'date_of_death', 'number_of_books', 'slug')

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'author', 'pub_date', 'isbn', 'slug',)

class CarouselSlideAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display = ('title', 'url', 'active','created_on',)

def mark_as_seen(modeladmin, request, queryset):
    queryset.update(seen=True)
mark_as_seen.short_description = "Mark Submissions as Seen"

def export_as_csv(modeladmin, request, queryset):
    timestamp = timezone.now()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mailing-list-{}-{}-{}.csv"'.format(timestamp.day, timestamp.month, timestamp.year)
    writer = csv.writer(response)
    writer.writerow(['Email', 'Subscribed On'])
    for submission in queryset:
        writer.writerow([submission.email, submission.created_on])
    return response
export_as_csv.short_description = "Download Selected as CSV"

class MailingListSubscriberAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)
    list_display = ('email', 'seen', 'created_on')
    actions = [ mark_as_seen, export_as_csv]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(CarouselSlide, CarouselSlideAdmin)
admin.site.register(MailingListSubscriber, MailingListSubscriberAdmin)
