from django.contrib import admin
from .models import Volunteer, Partner, Member, Caregiver

# Register your models here.
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "created_at")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("gender", "created_at")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("org_name", "contact_person", "org_email", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("org_name", "org_email")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("first_name", "last_name", "email", "national_id")


@admin.register(Caregiver)
class CaregiverAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "relationship", "member", "created_at")
    search_fields = ("first_name", "last_name", "national_id")