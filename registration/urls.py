from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('member/', views.member_registration, name='member'),
    path('caregiver/', views.caregiver_registration, name='caregiver'),
    path('partner/', views.partner_registration, name='partner'),
    path('volunteer/', views.volunteer_registration, name='volunteer'),
    path('volunteer/submit/', views.volunteer_registration_view, name='volunteer_submit'),
    path('partner/submit/', views.partner_registration_view, name='partner_submit'),
    path('member/submit/', views.member_registration_view, name='member_submit'),
    path('caregiver/submit/', views.caregiver_registration_view, name='caregiver_submit'),
]