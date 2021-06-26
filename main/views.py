from main.models import *
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserProfile
# Create your views here.

class HomeView(LoginRequiredMixin,View):
    def get(self, request):
        users = UserProfile.objects.all().order_by('?')[:4]
        context = {
            'user':users,
        }
        return render(request, 'index.html', context)


class MyPostsView(View):
    def get(self, request):
        posts = Posts.objects.filter(author=request.user.user_profile)
        blogs = Blogs.objects.filter(author=request.user.user_profile)
        context = {'post':posts, 'blog':blogs}
        return render(request, 'docs.html',context)


class AddPostView(View):
    def get(self, request):
        return render(request, 'addpost.html')

class FollowView(View):
    def get(self, request):
        users = UserProfile.objects.all().order_by('-id')
        context = {
            'user':users,
        }
        return render(request, 'orders.html',context)


class PostsView(View):
    def get(self, request):
        return render(request, 'index2.html')


class BlogsView(View):
    def get(self, request):
        return render(request, 'index3.html')

def postdetail(request):
        return render(request, 'post-det.html')