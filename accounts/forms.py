from typing import ClassVar
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import *
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","first_name",'last_name', "email", "password1", "password2"]
        widgets = {}

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['avatar','job','birth','place','phone',
        'telegram','github','python','php','js','java',
        'c','edu','edu_date','work','work_date','bio']


# class UpdateAvatar(forms.ModelForm):

#     class Meta:
#         model = UserProfile
#         fields = []
