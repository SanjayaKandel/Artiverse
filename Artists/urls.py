from django.urls import path
from . import views

urlpatterns = [
    path('Update_profile/',views.update_artist_profile, name='update_artist_profile'),
    path('Create_profile/',views.create_artist_profile, name='create_artist_profile'),
    path('profile/',views.artist_profile, name='artist_profile'),
    path('about_us/',views.about_page, name='artist_about_page'),
    
]