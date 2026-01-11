from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    # Administration URL patterns go here
    path('', views.login_view, name='admin_login'),
    path('dashboard/', views.dashboard_view, name='admin_dashboard'),
    path('login/', views.login_filled_view, name='admin_login_filled'),
    path('logout/', views.logout_view, name='admin_logout'),
    path('member/<int:pk>/edit/', views.member_update_view, name='member_edit'),
    path('member/<int:pk>/delete/', views.member_delete_view, name='member_delete'),
    path('caregiver/<int:pk>/edit/', views.caregiver_update_view, name='caregiver_edit'),
    path('caregiver/<int:pk>/delete/', views.caregiver_delete_view, name='caregiver_delete'),
    path('volunteer/<int:pk>/edit/', views.volunteer_update_view, name='volunteer_edit'),
    path('volunteer/<int:pk>/delete/', views.volunteer_delete_view, name='volunteer_delete'),
    path('partner/<int:pk>/edit/', views.partner_update_view, name='partner_edit'),
    path('partner/<int:pk>/delete/', views.partner_delete_view, name='partner_delete'),
    path('delivery/create/', views.delivery_create_view, name='delivery_create'),
    path('delivery/create/member/<int:member_pk>/', views.delivery_create_view, name='delivery_create_for_member'),
    path('delivery/<int:pk>/edit/', views.delivery_update_view, name='delivery_edit'),
    path('delivery/<int:pk>/delete/', views.delivery_delete_view, name='delivery_delete'),
    path('meal/create/', views.meal_create_view, name='meal_create'),
    path('meal/<int:pk>/edit/', views.meal_update_view, name='meal_edit'),
    path('meal/<int:pk>/delete/', views.meal_delete_view, name='meal_delete'),
    path('menu/create/', views.menu_create_view, name='menu_create'),
    path('menu/<int:pk>/edit/', views.menu_update_view, name='menu_edit'),
    path('menu/<int:pk>/delete/', views.menu_delete_view, name='menu_delete'),
    path('ingredient/create/', views.ingredient_create_view, name='ingredient_create'),
    path('ingredient/<int:pk>/edit/', views.ingredient_update_view, name='ingredient_edit'),
    path('ingredient/<int:pk>/delete/', views.ingredient_delete_view, name='ingredient_delete'),
]
