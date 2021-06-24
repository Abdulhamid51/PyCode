from django import forms
from .models import *

class AddPostForm(forms.ModelForm):

    class Meta:
        model = Posts
        feilds = '__all__'