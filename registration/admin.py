from django.contrib import admin
from .models import Volunteer

# Register your models here.
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "created_at")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("gender", "created_at")