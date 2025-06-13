from django.urls import path
from . import views
from login.views import page_not_found

app_name = "hotelapp"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/booking', views.booking, name='booking'),
    path('menu/', views.menu, name='menu'),
    path("add_to_cart/<int:product_id>/",views.add_to_cart, name='add_to_cart'),
    path("cart/",views.view_cart, name='view_cart'),
    path("place_order/", views.place_order, name="place_order"),
    path("error/", page_not_found, name="page_not_found"),
]
