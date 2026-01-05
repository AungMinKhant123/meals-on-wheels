from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('member/', views.member_registration, name='member'),
    path('caregiver/', views.caregiver_registration, name='caregiver'),
    path('partner/', views.partner_registration, name='partner'),
    path('volunteer/', views.volunteer_registration, name='volunteer'),
]