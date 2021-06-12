from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class PostsView(View):
    def get(self, request):
        return render(request, 'index2.html')


class BlogsView(View):
    def get(self, request):
        return render(request, 'index3.html')