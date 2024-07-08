from django.urls import path
from . import views
urlpatterns=[
    path('create_user/',views.create_user, name='create_user'),
    path('update_user/',views.update_user, name='update_user'),
    path('user_profile/',views.user_profile, name='user_profile'),
    path('address/',views.billing_address, name='billing_address'),
    path('view/artist_profile/<int:artist_id>/',views.artist_profile_view, name='artist_profile_view'),

]