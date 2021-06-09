from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.db.models.fields import IPAddressField
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
	name = models.CharField('category', max_length=100)
	slug = models.SlugField('slug', max_length=100)

	def __str__(self):
		return self.name


class Tag(model.Model):
	name = models.CharField('tag', max_length=100)
	slug = models.SlugField('slug', max_length=100)
	color = models.CharField('color', max_length=100)

	def __str__(self):
		return self.name


class Posts(models.Model):
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post', null=True)
	title = models.CharField('title',max_length=500)
	tag = models.ManyToManyField(Tag, related_name='posts', null=True)
	date = models.DateTimeField('date',auto_add_now=True)
	body = RichTextField('body')
	slug = models.SlugField('slug', max_length=30)

	def __str__(self):
		return self.title

class Blogs(models.Model):
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_blog', null=True)
	title = models.CharField('title',max_length=500)
	category = models.ForeignKey(Category, related_name='blogs', on_delete=models.PROTECT, null=True)
	date = models.DateTimeField('date',auto_add_now=True)
	image = models.ImageField('image', upload_to='blogs/', blank=True)
	body = RichTextField('body')
	slug = models.SlugField('slug', max_length=30)

	def __str__(self):
		return self.title

