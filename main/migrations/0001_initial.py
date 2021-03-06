# Generated by Django 3.2.1 on 2021-06-12 11:27

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='tag')),
                ('slug', models.SlugField(max_length=100, verbose_name='slug')),
                ('color', models.CharField(max_length=100, verbose_name='color')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('slug', models.SlugField(max_length=30, verbose_name='slug')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to='accounts.userprofile')),
                ('tag', models.ManyToManyField(related_name='posts', to='main.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='title')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('image', models.ImageField(blank=True, upload_to='blogs/', verbose_name='image')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('slug', models.SlugField(max_length=30, verbose_name='slug')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_blog', to='accounts.userprofile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogs', to='main.category')),
            ],
        ),
    ]
