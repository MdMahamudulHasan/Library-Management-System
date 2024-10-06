from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import render
from .models import staffProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



def staff_account_create(request):
    if request.method =='POST':
        staff_first_name = request.POST['staff_firstName']
        staff_last_name = request.POST['staff_tName']
        staff_phone_number = request.POST['staff_phn']
        staff_user_name = request.POST['staff_user']
        staff_department = request.POST['staff_department']
        staff_email = request.POST['staff_email']
        staff_position = request.POST['staff_position']
        staff_password = request.POST['staff_password']
        
        staff = staffProfile(
            staff_first_name = staff_first_name,
            staff_last_name = staff_last_name,
            staff_phone_number = staff_phone_number,
            staff_user_name = staff_user_name,
            staff_department = staff_department,
            staff_email = staff_email,
            staff_position = staff_position,
            staff_password = staff_password
        )
        
        staff.save()
        return redirect(f'/staff-login/?email ={staff_email} & password={staff_password}')
    
    
    return render(request, 'staffaccountcreate.html')




from django.contrib import messages
from django.shortcuts import redirect, render
from .models import staffProfile

def staff_login(request):
    if request.method == 'POST':
        staff_email = request.POST['staff_email']
        staff_password = request.POST['staff_password']

        try:
            # Authenticate staff manually
            staff = staffProfile.objects.get(staff_email=staff_email, staff_password=staff_password)
            
            # Set session for staff
            request.session['staff_id'] = staff.id  
            messages.success(request, f"Staff {staff_email} logged in successfully.")
            
            # Redirect to staff profile or default page
            next_url = request.GET.get('next', 'staff_profile')
            return redirect(next_url)

        except staffProfile.DoesNotExist:
            
            messages.error(request, 'Invalid email or password')
            return redirect('staff_login')

    return render(request, 'stafflogin.html')




def staff_profilePage(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:  
        return redirect('staff_login')

    try:
        staff = staffProfile.objects.get(id=staff_id)
    except staffProfile.DoesNotExist:
        
        return redirect('staff_login')

    if not request.user.is_authenticated:
        return render(request, 'staffprofile.html', {'staff': staff, 'error': 'User not authenticated.'})

    return render(request, 'staffprofile.html', {'staff': staff})



from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from books.models import BookingRequest

# Check if user is staff
def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def view_booking_requests(request):
    # pending booking requests
    bookings = BookingRequest.objects.filter(status__in=['pending', 'confirmed'])

    return render(request, 'booking_requests.html', {'bookings': bookings})


@user_passes_test(is_staff)
def update_booking_status(request, booking_id, action):
    booking = get_object_or_404(BookingRequest, id=booking_id)

    if action == 'confirm':
        booking.status = 'confirmed'
        booking.issue_date = request.POST.get('issue_date')  # Capture issue date
        booking.return_date = request.POST.get('return_date')  # Capture return date
    elif action == 'decline':
        booking.status = 'declined'

    booking.save()

    return redirect('view-booking-requests')
