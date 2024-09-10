from django.urls import path
from . import views
urlpatterns=[
    path('create',views.create_user, name='create_user'),
    path('update',views.update_user, name='update_user'),
    path('view/profile/',views.user_profile, name='user_profile'),
    path('address/',views.billing_address, name='billing_address'),
    path('view/artist/profile/<int:artist_id>/',views.artist_profile_view, name='artist_profile_view'),
    path('exhibition/list/',views.exhibition, name='exhibition'),
    path('view/exhibition/<int:exhibition_id>/',views.view_exhibitions, name='view_exhibition'),
    
#<---------ordered and favourites item--------->
path('ordered_items/',views.ordered_items, name='ordered_items'),
path('favourite_list/',views.favourites_list, name='favourite_list'),
    

]