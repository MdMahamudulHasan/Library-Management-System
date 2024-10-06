from django.contrib import admin
from .models import bookModel, BookingRequest

# bookModel display
class bookModelAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_edition', 'book_publisher', 'books_department', 'course_code')
    search_fields = ('book_title', 'book_publisher', 'books_department', 'course_code')
    list_filter = ('books_department', 'course_code')
    readonly_fields = ('book_image', 'book_pdf')

# BookingRequest display
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'issue_date', 'return_date', 'request_date')
    search_fields = ('user__username', 'book__book_title', 'status')
    list_filter = ('status', 'request_date')
    readonly_fields = ('request_date',)

# Register the models 
admin.site.register(bookModel, bookModelAdmin)
admin.site.register(BookingRequest, BookingRequestAdmin)
