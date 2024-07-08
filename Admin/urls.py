from django.urls import path
from . import views

urlpatterns = [
    path('exhibitions/', views.exhibition_list, name='exhibition_list'),
    path('exhibition/<int:exhibition_id>/', views.exhibition_detail, name='exhibition_detail'),
    path('exhibitions/add/', views.add_exhibition, name='add_exhibition'),
]
