
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone_number = models.CharField(max_length=15)
    university_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    registration_no = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pics/default.jpg')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
