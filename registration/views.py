from django.shortcuts import render
from .models import Volunteer, Partner, Member, Caregiver

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


def member_registration_view(request):
    if request.method == "POST":
        Member.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            national_id=request.POST.get("national_id"),
            gender=request.POST.get("gender"),
            dob=request.POST.get("dob"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            postal_code=request.POST.get("postal_code"),
            health_conditions=request.POST.get("health_conditions"),
            dietary_restrictions=request.POST.get("dietary_restrictions"),
        )

        return render(request, "registration/member.html", {
            "success": True
        })

    return render(request, "registration/member.html")

def caregiver_registration_view(request):
    if request.method == "POST":

        # Create Member
        member = Member.objects.create(
            first_name=request.POST.get("member_first_name"),
            last_name=request.POST.get("member_last_name"),
            national_id=request.POST.get("member_id"),
            dob=request.POST.get("member_dob"),
            gender=request.POST.get("gender"),
            email=request.POST.get("caregiver_email"),
            phone=request.POST.get("caregiver_phone"),
            address=request.POST.get("caregiver_address"),
            postal_code=request.POST.get("postal_code"),
            health_conditions=request.POST.get("member_health"),
            dietary_restrictions=request.POST.get("member_diet"),
        )

        # Create Caregiver linked to Member
        Caregiver.objects.create(
            member=member,
            first_name=request.POST.get("caregiver_first_name"),
            last_name=request.POST.get("caregiver_last_name"),
            national_id=request.POST.get("caregiver_id"),
            gender=request.POST.get("caregiver_gender"),
            dob=request.POST.get("caregiver_dob"),
            relationship=request.POST.get("relationship"),
            email=request.POST.get("caregiver_email"),
            phone=request.POST.get("caregiver_phone"),
            address=request.POST.get("caregiver_address"),
        )

        return render(request, "registration/caregiver.html", {
            "success": True
        })

    return render(request, "registration/caregiver.html")