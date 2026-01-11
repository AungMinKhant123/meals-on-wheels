from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from registration.models import Member, Caregiver, Volunteer, Partner
from datetime import date
from django.db.models import Sum
from core.models import Donation, Delivery
from core.models import Ingredient
from core.forms import IngredientForm
from registration.forms import MemberForm, CaregiverForm, VolunteerForm, PartnerForm
from core.forms import DeliveryForm, MealForm, MenuForm
from core.models import Meal, Menu
from core.forms import DeliveryForm

# Create your views here.
def login_view(request):
    return render(request, 'administration/login.html')

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser, login_url='administration:admin_login')
def dashboard_view(request):
    members = Member.objects.order_by('-created_at')[:100]
    caregivers = Caregiver.objects.select_related('member').order_by('-created_at')[:100]
    volunteers = Volunteer.objects.order_by('-created_at')[:100]
    partners = Partner.objects.order_by('-created_at')[:100]
    donations = Donation.objects.order_by('-created_at')[:100]
    deliveries = Delivery.objects.select_related('member', 'volunteer', 'partner').order_by('-created_at')[:100]
    meals = Meal.objects.order_by('-created_at')[:100]
    menus = Menu.objects.order_by('-date')[:20]
    ingredients = Ingredient.objects.order_by('expiry_date')[:200]
    meals_delivered_count = Delivery.objects.filter(status='completed').count()
    active_members_count = Member.objects.filter(is_active=True).count()
    volunteers_count = Volunteer.objects.count()
    caregiver_count = Caregiver.objects.count()
    partner_count = Partner.objects.count()
    funds_raised_agg = Donation.objects.filter(status='completed').aggregate(total=Sum('amount'))
    funds_raised = funds_raised_agg.get('total') or 0
    events_count = Menu.objects.count()
    feedbacks_count = donations.count()
    context = {
        'members': members,
        'caregivers': caregivers,
        'volunteers': volunteers,
        'partners': partners,
        'donations': donations,
        'deliveries': deliveries,
        'meals': meals,
        'menus': menus,
        'ingredients': ingredients,
        'meals_delivered_count': meals_delivered_count,
        'active_members_count': active_members_count,
        'volunteers_count': volunteers_count,
        'caregiver_count': caregiver_count,
        'partner_count': partner_count,
        'funds_raised': funds_raised,
        'events_count': events_count,
        'feedbacks_count': feedbacks_count,
        'today': date.today(),
    }
    return render(request, 'administration/dashboard.html', context)


@user_passes_test(is_superuser, login_url='administration:admin_login')
def member_update_view(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = MemberForm(instance=member)

    return render(request, 'administration/member_form.html', {'form': form, 'member': member})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def member_delete_view(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/member_confirm_delete.html', {'member': member})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def caregiver_update_view(request, pk):
    caregiver = get_object_or_404(Caregiver, pk=pk)
    if request.method == 'POST':
        form = CaregiverForm(request.POST, instance=caregiver)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = CaregiverForm(instance=caregiver)

    return render(request, 'administration/caregiver_form.html', {'form': form, 'caregiver': caregiver})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def caregiver_delete_view(request, pk):
    caregiver = get_object_or_404(Caregiver, pk=pk)
    if request.method == 'POST':
        caregiver.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/caregiver_confirm_delete.html', {'caregiver': caregiver})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def volunteer_update_view(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = VolunteerForm(instance=volunteer)

    return render(request, 'administration/volunteer_form.html', {'form': form, 'volunteer': volunteer})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def volunteer_delete_view(request, pk):
    volunteer = get_object_or_404(Volunteer, pk=pk)
    if request.method == 'POST':
        volunteer.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/volunteer_confirm_delete.html', {'volunteer': volunteer})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def partner_update_view(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = PartnerForm(instance=partner)

    return render(request, 'administration/partner_form.html', {'form': form, 'partner': partner})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def partner_delete_view(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        partner.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/partner_confirm_delete.html', {'partner': partner})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def delivery_create_view(request, member_pk=None):
    initial = {}
    if member_pk:
        initial['member'] = member_pk

    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = DeliveryForm(initial=initial)

    return render(request, 'administration/delivery_form.html', {'form': form})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def delivery_update_view(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = DeliveryForm(instance=delivery)

    return render(request, 'administration/delivery_form.html', {'form': form, 'delivery': delivery})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def delivery_delete_view(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    if request.method == 'POST':
        delivery.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/delivery_confirm_delete.html', {'delivery': delivery})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def meal_create_view(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = MealForm()

    return render(request, 'administration/meal_form.html', {'form': form})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def meal_update_view(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = MealForm(instance=meal)

    return render(request, 'administration/meal_form.html', {'form': form, 'meal': meal})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def meal_delete_view(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/meal_confirm_delete.html', {'meal': meal})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def menu_create_view(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = MenuForm()

    return render(request, 'administration/menu_form.html', {'form': form})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def menu_update_view(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = MenuForm(instance=menu)

    return render(request, 'administration/menu_form.html', {'form': form, 'menu': menu})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def menu_delete_view(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/menu_confirm_delete.html', {'menu': menu})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def ingredient_create_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = IngredientForm()

    return render(request, 'administration/ingredient_form.html', {'form': form})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def ingredient_update_view(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('administration:admin_dashboard')
    else:
        form = IngredientForm(instance=ingredient)

    return render(request, 'administration/ingredient_form.html', {'form': form, 'ingredient': ingredient})


@user_passes_test(is_superuser, login_url='administration:admin_login')
def ingredient_delete_view(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('administration:admin_dashboard')

    return render(request, 'administration/ingredient_confirm_delete.html', {'ingredient': ingredient})

def login_filled_view(request):

    if request.method == 'POST':
        # Handle login logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add authentication logic as needed

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('administration:admin_dashboard')
        else:
            # Invalid login
            return render(request, 'administration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'administration/login.html')

def logout_view(request):
    logout(request)
    return redirect('administration:admin_login')