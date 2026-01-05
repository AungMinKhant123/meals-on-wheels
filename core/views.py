from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Donation
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def donate(request):
    return render(request, 'core/donate.html')

def donate_view(request):
    if request.method == "POST":
        amount = request.POST.get("amount")

        if not amount or float(amount) <= 0:
            messages.error(request, "Invalid donation amount.")
            return render(request, "core/donate.html")

        Donation.objects.create(
            amount=amount,
            status="completed"
        )
        
        # Add the success message
        messages.success(request, f"Thank you! Your donation of ${amount} was successful.")
        return redirect("core:donated") # Redirect to clear the POST data

    return render(request, "core/donate.html")