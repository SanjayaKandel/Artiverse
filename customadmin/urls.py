from django.urls import path
from . import views
urlpatterns=[
    # path('dashboard/', views.custom_admin, name='admin' ),
    path('profile/', views.admin_profile, name='admin_profile'),
    path('create/profile',views.create_admin_profile, name='create_admin'),
    
    # <------ managing user and artwork data------>
    
    path('artwork/manage/', views.view_artwork, name='view_artwork'),
    path('delete_artwork/<int:artwork_id>/', views.delete_artwork, name='delete_artwork'),
    path('user/manage/', views.manage_user, name='manage_user'),
    path('user/delete/<int:id>/', views.delete_user, name='delete_user'),
    path('artist/manage/', views.manage_artist, name='manage_artist'),
    path('delete/artist/<int:id>/', views.delete_artist, name='delete_artist'),
    
    #<------ view pages------->
    path('view/artwork/<int:id>/',views.artwork_view_admin ,name='view_artwork_admin'),
    path('view/user/<int:id>/',views.user_view_admin ,name='view_user_admin'),
    path('view/artist/<int:id>/',views.artist_view_admin ,name='view_artist_admin'),
    
    #<---------exhibition-------->
    path('create-exhibition/', views.create_exhibition, name='create_exhibition'),
    path('view/exhibitions/', views.exhibition_list, name='exhibition_list'),
    path('add/exhibition', views.add_to_exhibition, name='add_to_exhibition'),
     path('exhibition/<int:exhibition_id>/', views.exhibition_details, name='exhibition_details'),
]