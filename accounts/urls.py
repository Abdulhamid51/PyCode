from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'accounts'

urlpatterns = [
    path("profile/update", ProfileUpdateView.as_view(), name="update_profile"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profiles/<slug>", UserDetailView.as_view(), name="user_detail"),
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", Register.as_view(), name="register"),
]   