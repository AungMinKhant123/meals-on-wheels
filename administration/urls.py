from django.urls import path
from . import views

app_name = 'administration'

urlpatterns = [
    # Administration URL patterns go here
    path('', views.login_view, name='admin_login'),
    path('dashboard/', views.dashboard_view, name='admin_dashboard'),
    path('login/', views.login_filled_view, name='admin_login_filled'),
    path('logout/', views.logout_view, name='admin_logout'),
]
