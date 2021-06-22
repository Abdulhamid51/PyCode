from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import View

import rstr

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from .models import *
from main.models import Category, Posts
from .forms import *
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class ProfileView(LoginRequiredMixin, View):

	def get(self, request):
		form = UpdateAvatar(request.GET)
		return render(request, 'account.html',{'form':form})




class ProfileUpdateView(LoginRequiredMixin, UpdateView):
	model = UserProfile
	form_class = UpdateProfileForm
	success_url = '/accounts/profile'
	template_name = 'settings.html'


class Register(View):
	def get(self,request):
		form = RegisterForm(request.GET)
		context = {'form':form}
		return render(request,'signup.html', context)

	def post(self,request):
		form = RegisterForm(request.POST)
		if form.is_valid():
			print('@'*50)
			u = form.save()
			try:
				user = UserProfile.objects.create(user=u,slug=u.username)
				user.save()
			except:
				user = None
			HttpResponseRedirect('/')
		else:
			print('#'*50)
			form = RegisterForm()

		context = {'form':form}
		return render(request,'signup.html', context)