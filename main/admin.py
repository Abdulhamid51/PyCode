from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Posts)
admin.site.register(Blogs)
admin.site.register(Tag)
admin.site.register(Category)