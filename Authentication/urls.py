from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('artist/', views.artist, name='artist'),
    path('logout/', views.logout_view, name='logout_view'),
    path('verify-email/<str:key>/', views.VerifyEmail.as_view(), name='verify_email'),
    path('verify-email-success/', TemplateView.as_view(template_name="Authentication/verify_email_success.html"), name='verify_email_success'),
    path('email-confirmation/<key>/', views.CustomConfirmEmailView.as_view(), name='account_confirm_email'),
]
