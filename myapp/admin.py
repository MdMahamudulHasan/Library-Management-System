from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'university_name', 'department', 'batch', 'registration_no')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'university_name', 'department', 'registration_no')
    list_filter = ('university_name', 'department', 'batch')
    readonly_fields = ('profile_picture',)
    
    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

# Register the model
admin.site.register(UserProfile, UserProfileAdmin)
