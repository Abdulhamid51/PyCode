from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'accounts'

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/<pk>", ProfileUpdateView.as_view(), name="update_profile"),
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", Register.as_view(), name="register"),
]