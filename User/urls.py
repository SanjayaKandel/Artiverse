from django.urls import path
from . import views
urlpatterns=[
    path('create',views.create_user, name='create_user'),
    path('update',views.update_user, name='update_user'),
    path('view/profile/',views.user_profile, name='user_profile'),
    path('address/',views.billing_address, name='billing_address'),
    path('view/artist/profile/<int:artist_id>/',views.artist_profile_view, name='artist_profile_view'),

]