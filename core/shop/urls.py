from django.urls import path
from .views import *

urlpatterns = [
  path('',home, name='home'),
  path('register',register, name='register'),
  path('login',login_page, name='login'),
  path('logout',logout_page, name='logout'),
  path('collections/',collections, name='collections'),
  path('collections/<str:name>',collectionsview, name='collections'),
  path('collections/<str:cname>/<str:pname>',product_details, name='product_details'),
  path('addtocart', add_to_cart ,name='addtocart'),
  path('cart', cart_page ,name='cart'),
  path('remove_cart/<str:cid>', remove_cart ,name='remove_cart'),
  path('fav', fav_page ,name='fav'),
  path('favviewpage', fav_view_page ,name='favviewpage'),
  path('remove_fav/<str:fid>',remove_fav,name="remove_fav"),
]