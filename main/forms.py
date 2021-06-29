from django import forms
from .models import *

class AddPostForm(forms.ModelForm):

    class Meta:
        model = Posts
        feilds = ['title','tag','body']
        exclude = ('author','slug')