from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="index"),
    path('explore/',views.explore, name="explore"),
    path('query/',views.search, name="query"),
    path('about/',views.about_page, name="about"),
    path('artist/list/',views.artist_list, name="artist_list"),
    path('add_to_cart/<int:artwork_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
    
]