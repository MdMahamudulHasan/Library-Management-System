from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from books.models import bookModel
from django.shortcuts import render, get_object_or_404



def displayBook(request):
    query = request.GET.get('search')
    if query:
        # Filter books by title, course code, or publisher name 
        books = bookModel.objects.filter(
            book_title__icontains=query
        ) | bookModel.objects.filter(
            course_code__icontains=query
        ) | bookModel.objects.filter(
            book_publisher__icontains=query
        )
    else:
        
        books = bookModel.objects.all().order_by('-id')[:10]  #  limit to 10

    return render(request, 'displayBook.html', {'books': books})





def addBook(request):
    if request.method == 'POST':
        book_title = request.POST.get('booksTitle')
        book_edition = request.POST.get('bookEdition')
        book_id = request.POST.get('bookId')
        book_publisher = request.POST.get('publisherName')
        books_department = request.POST.get('bookDepartment')
        course_code = request.POST.get('courseCode')
        book_description = request.POST.get('bookDescription')
        book_image = request.FILES.get('bookImage') 
        book_pdf = request.FILES.get('bookPDF')      
        
        books_Object = bookModel(
            book_title=book_title,
            book_edition=book_edition,
            book_id=book_id,
            book_publisher=book_publisher,
            books_department=books_department,
            course_code=course_code,  
            book_description=book_description,
            book_image=book_image,
            book_pdf=book_pdf
        )
        
        books_Object.save()
        messages.success(request, "Book added successfully!")
        return redirect('add-book')

    return render(request, 'addbook.html')





def requestPage(request):
    return render(request, 'requestPage.html')


def bookDetailsPage(request, book_id):
    # Retrieve the book based on its ID
    book = get_object_or_404(bookModel, id=book_id)

    return render(request, 'bookDetails.html', {'book': book})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BookingRequest, bookModel


def book_booking(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(bookModel, id=book_id)

        # Create a booking request
        booking = BookingRequest.objects.create(
            user=request.user,
            book=book,
        )
        booking.save()

        
        return redirect('display-Book')



from django.contrib.auth.decorators import user_passes_test


def is_staff(user):
    return user.is_staff


def view_booking_requests(request):
    bookings = BookingRequest.objects.filter(status__in=['pending', 'confirmed']).order_by('-request_date')
    return render(request, 'booking_requests.html', {'bookings': bookings})


def update_booking_status(request, booking_id, action):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    if action == 'confirm' and request.method == 'POST':
        issue_date = request.POST.get('issue_date')
        return_date = request.POST.get('return_date')
        
        if issue_date and return_date:
            booking.issue_date = issue_date
            booking.return_date = return_date
            booking.status = 'confirmed'
            booking.save()
            messages.success(request, f"Booking for {booking.book.book_title} confirmed with issue date: {issue_date}.")
        else:
            messages.error(request, "Both issue date and return date are required to confirm the booking.")

    elif action == 'return':
        # Mark the booking status as "Book Returned"
        booking.status = 'Book Returned'
        booking.save()

        user_profile = booking.user.userprofile 
        user_profile.save()

        messages.success(request, f"Book '{booking.book.book_title}' has been marked as 'Book Returned'.")

    elif action == 'decline':
        booking.status = 'declined'
        booking.save()
        messages.success(request, f"Booking for {booking.book.book_title} declined.")

    return redirect('view-booking-requests')