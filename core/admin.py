from django.contrib import admin
from .models import Donation

# Register your models here.
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("amount", "status", "created_at")
    list_filter = ("status", "created_at")