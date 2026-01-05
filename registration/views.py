from django.shortcuts import render

# Create your views here.
def member_registration(request):
    return render(request, 'registration/member.html')

def caregiver_registration(request):
    return render(request, 'registration/caregiver.html')

def partner_registration(request):
    return render(request, 'registration/partner.html')

def volunteer_registration(request):
    return render(request, 'registration/volunteer.html')