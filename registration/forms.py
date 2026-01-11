from django import forms
from .models import Member, Caregiver, Volunteer, Partner


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'first_name',
            'last_name',
            'national_id',
            'gender',
            'dob',
            'email',
            'phone',
            'address',
            'postal_code',
            'health_conditions',
            'dietary_restrictions',
            'is_active',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2}),
            'health_conditions': forms.Textarea(attrs={'rows': 2}),
            'dietary_restrictions': forms.Textarea(attrs={'rows': 2}),
        }


class CaregiverForm(forms.ModelForm):
    class Meta:
        model = Caregiver
        fields = [
            'member',
            'first_name',
            'last_name',
            'national_id',
            'gender',
            'dob',
            'relationship',
            'email',
            'phone',
            'address',
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = [
            'first_name',
            'last_name',
            'gender',
            'email',
            'phone',
            'address',
            'postal_code',
            'interests',
            'availability',
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'interests': forms.Textarea(attrs={'rows': 2}),
            'availability': forms.Textarea(attrs={'rows': 2}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = [
            'org_name',
            'contact_person',
            'org_email',
            'org_phone',
            'org_address',
            'org_postal',
            'services',
            'additional_info',
            'is_approved',
        ]
        widgets = {
            'org_address': forms.Textarea(attrs={'rows': 2}),
            'additional_info': forms.Textarea(attrs={'rows': 2}),
        }
