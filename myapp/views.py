from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import authenticate, login



def homePage(request):
    
    print(request.user.is_authenticated)  
    return render(request, 'home.html')







def teamPage(request):
    return render(request, 'team.html')



def account_createPage(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('firstName')
            last_name = request.POST.get('lastName')  # Fixed field name
            phone_number = request.POST.get('phn')
            university_name = request.POST.get('uniname')
            user_name = request.POST.get('user')
            department = request.POST.get('department')
            email = request.POST.get('mail')
            batch = request.POST.get('batch')
            registration_no = request.POST.get('regNo')
            password = request.POST.get('password')

            if not all([first_name, last_name, phone_number, university_name, user_name, department, email, password]):
                messages.error(request, "All required fields must be filled.")
                return redirect('account-create')

            try:
                user = User.objects.create_user(
                    username=user_name,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
            except Exception as e:
                messages.error(request, "Error creating user: " + str(e))
                return redirect('account-create')

            user_profile = UserProfile(
                user=user,
                phone_number=phone_number,
                university_name=university_name,
                department=department,
                batch=batch,
                registration_no=registration_no
            )
            user_profile.save()

            messages.success(request, "Account created successfully!")
            return redirect('login')

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('account-create')

    return render(request, 'account-create.html')








def loginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # (assuming email is unique)
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Authenticate using the username to the email
            user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, f"User {email} logged in successfully.")
            return redirect('profile')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'login.html')





def update_profile_picture(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)

        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
            user_profile.save()

            return JsonResponse({
                'status': 'success',
                'new_profile_picture_url': user_profile.profile_picture.url
            })

        return JsonResponse({'status': 'error', 'message': 'No file uploaded'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



from django.core.exceptions import ObjectDoesNotExist

@login_required
def profilePage(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If the profile doesn't exist
        messages.error(request, 'Please complete your profile information.')
        return redirect('account-create')  # Redirect to create profile page

    if request.method == 'POST':
        
        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']
            user_profile.profile_picture = profile_picture
            user_profile.save()
            messages.success(request, 'Profile picture updated successfully!')
            return redirect('profile')

    # student's booking history
    booking_history = BookingRequest.objects.filter(user=request.user, status='confirmed')

    return render(request, 'profile.html', {
        'user_profile': user_profile,
        'booking_history': booking_history,
    })  
    
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import BookingRequest, bookModel 

@login_required
def book_booking(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(bookModel, id=book_id)

        booking, created = BookingRequest.objects.get_or_create(
            user=request.user,
            book=book,
            status='pending'
        )

        if created:
            booking.save()
            messages.success(request, "Your booking request has been submitted!")
        else:
            messages.warning(request, "You already have a pending booking for this book.")

        return redirect('display-Book')
