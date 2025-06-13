from django.urls import path
from .views import login, logout, userinfo, page_not_found

app_name = "loginapp"
urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("user/", userinfo, name="user"),
    path("error/", page_not_found, name="page_not_found"),
]