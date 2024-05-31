from django.contrib import admin

from user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin with all fields """
    list_display = ["user", "bio"]
    search_fields = ["user", "bio"]
    list_filter = ["user", "bio"]
    list_per_page = 50
