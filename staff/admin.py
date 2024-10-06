from django.contrib import admin
from .models import staffProfile
from django.contrib.auth.hashers import make_password

class StaffProfileAdmin(admin.ModelAdmin):

    list_display = ('staff_first_name', 'staff_last_name', 'staff_department', 'staff_email', 'staff_position')

    search_fields = ('staff_first_name', 'staff_last_name', 'staff_email', 'staff_department')


    list_filter = ('staff_department', 'staff_position')


    fields = ('staff_first_name', 'staff_last_name', 'staff_user_name', 'staff_department', 
            'staff_position', 'staff_email', 'staff_phone_number', 'staff_password')


    def save_model(self, request, obj, form, change):
        if obj.staff_password:
            obj.staff_password = make_password(obj.staff_password)
        super().save_model(request, obj, form, change)


admin.site.register(staffProfile, StaffProfileAdmin)