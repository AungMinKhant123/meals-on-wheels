from django.shortcuts import render
from .models import Volunteer, Partner

# Create your views here.
def member_registration(request):
    return render(request, 'registration/member.html')

def caregiver_registration(request):
    return render(request, 'registration/caregiver.html')

def partner_registration(request):
    return render(request, 'registration/partner.html')

def volunteer_registration(request):
    return render(request, 'registration/volunteer.html')

def volunteer_registration_view(request):
    if request.method == "POST":
        interests = request.POST.getlist("interests")

        Volunteer.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get("gender"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            postal_code=request.POST.get("postal_code"),
            interests=interests,
            availability=request.POST.get("availability"),
        )

        return render(request, "registration/volunteer.html", {
            "success": True
        })

    return render(request, "registration/volunteer.html")

def partner_registration_view(request):
    if request.method == "POST":
        services = request.POST.getlist("services")

        Partner.objects.create(
            org_name=request.POST.get("org_name"),
            contact_person=request.POST.get("contact_person"),
            org_email=request.POST.get("org_email"),
            org_phone=request.POST.get("org_phone"),
            org_address=request.POST.get("org_address"),
            org_postal=request.POST.get("org_postal"),
            services=services,
            additional_info=request.POST.get("org_additional_info"),
        )

        return render(request, "registration/partner.html", {
            "success": True
        })

    return render(request, "registration/partner.html")