from django import forms
from .models import Delivery, Meal, Menu, Ingredient
from registration.models import Volunteer, Partner


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['member', 'volunteer', 'partner', 'delivery_date', 'status']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit volunteers/partners to those offering delivery service
        try:
            self.fields['volunteer'].queryset = Volunteer.objects.filter(interests__contains=['delivery'])
        except Exception:
            pass
        try:
            self.fields['partner'].queryset = Partner.objects.filter(services__contains=['delivery'])
        except Exception:
            pass


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'ingredients', 'prep_instructions', 'prep_time_minutes']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'expiry_date', 'status']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['date', 'meals', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

