from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("posts/", PostsView.as_view(), name="posts"),
    path("blogs/", BlogsView.as_view(), name="blogs"),
]