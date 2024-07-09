from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordChangeView,
    # CustomPasswordResetCompleteView,
    # CustomPasswordChangeDoneView
)

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('artist/', views.artist, name='artist'),
    
    # verify email urls
    
    path('logout/', views.logout_view, name='logout_view'),
    path('verify-email/<str:key>/', views.VerifyEmail.as_view(), name='verify_email'),
    path('verify-email-success/', TemplateView.as_view(template_name="Authentication/verify_email_success.html"), name='verify_email_success'),
    path('email-confirmation/<key>/', views.CustomConfirmEmailView.as_view(), name='account_confirm_email'),
    
    # pass reset urls
    
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # password change urls
    
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

]
