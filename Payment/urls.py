# urls.py

from django.urls import path
from .views import payment_success, payment_failure

urlpatterns = [
    path('success/', payment_success, name='payment_success'),
    path('failure/', payment_failure, name='payment_failure'),
]
