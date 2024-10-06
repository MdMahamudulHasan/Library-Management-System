from django.db import models

class staffProfile(models.Model):
    staff_first_name = models.CharField(max_length=100)
    staff_last_name = models.CharField(max_length=100)
    staff_phone_number = models.CharField(max_length=15)
    staff_user_name = models.CharField(max_length=50)
    staff_department = models.CharField(max_length=100)
    staff_position = models.CharField(max_length=50)
    staff_email = models.EmailField(unique=True)
    staff_password = models.CharField(max_length=100)
    
