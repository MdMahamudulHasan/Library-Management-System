"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views as library_views
from myapp import views as myapp_views
from django.contrib.auth.views import LogoutView
from staff import views as staff_views
from books import views as book_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.homePage, name="home"),
    path('login/', myapp_views.loginPage, name="login"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  
    path('account-create/', myapp_views.account_createPage, name="account-create"),
    path('profile/', myapp_views.profilePage, name="profile"),
    path('team/', myapp_views.teamPage, name="team"),
    path('update-profile-picture/', myapp_views.update_profile_picture, name='update-profile-picture'),

    # Staff views
    path('staff-login/', staff_views.staff_login, name="staff_login"),
    path('staff-profile/', staff_views.staff_profilePage, name="staff_profile"),
    path('staff-account-create/', staff_views.staff_account_create, name="staff_account_create"),
    
    
    #books views
    path('add-book/', book_views.addBook, name="add-book"),
    path('books/', book_views.displayBook, name="display-Book"),
    path('request-page/', book_views.requestPage, name="request-page"),
    path('book/<int:book_id>/', book_views.bookDetailsPage, name='book-details'),
    
    #Booking-related URLs
    path('book-booking/', book_views.book_booking, name='book-booking'),
    path('booking-requests/', book_views.view_booking_requests, name='view-booking-requests'),
    path('update-booking-status/<int:booking_id>/<str:action>/', book_views.update_booking_status, name='update-booking-status'),
    
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
