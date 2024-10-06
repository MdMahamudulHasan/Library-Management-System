from django.db import models
from django.contrib.auth.models import User 
# using Django's User model

class bookModel(models.Model):
    book_title = models.CharField(max_length=100)
    book_edition = models.CharField(max_length=50)
    book_id = models.CharField(max_length=50)
    book_publisher = models.CharField(max_length=100)
    books_department = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    book_description = models.CharField(max_length=300)
    book_image = models.ImageField(upload_to='books_pictures/')
    book_pdf = models.FileField(upload_to='books_pdf/')
    
    def __str__(self):
        return self.book_title

class BookingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(bookModel, on_delete=models.CASCADE)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('declined', 'Declined')], default='pending')
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.book_title}"
