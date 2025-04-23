from django.urls import path
from .views import register, login, logout, userinfo

app_name = "loginapp"
urlpatterns = [
    path('login/register/', register, name='register'),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("user/", userinfo, name="user"),
]