# Generated by Django 3.2.1 on 2021-06-12 11:27

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='rang nomi')),
                ('color', models.CharField(max_length=300, verbose_name='rangi')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Kasbingiz')),
                ('job_slug', models.SlugField(verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, verbose_name='userslug')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_avatars/', verbose_name='avatar image')),
                ('birth', models.DateField(blank=True, null=True, verbose_name="Tug'ilgan Kuningiz")),
                ('place', models.CharField(blank=True, max_length=250, null=True, verbose_name='place')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Telefon raqam')),
                ('telegram', models.CharField(blank=True, max_length=200, null=True, verbose_name='telegram')),
                ('github', models.CharField(blank=True, max_length=200, null=True, verbose_name='github')),
                ('python', models.CharField(blank=True, max_length=2, verbose_name='Python')),
                ('php', models.CharField(blank=True, max_length=2, verbose_name='PHP')),
                ('js', models.CharField(blank=True, max_length=2, verbose_name='JS')),
                ('java', models.CharField(blank=True, max_length=2, verbose_name='Java')),
                ('c', models.CharField(blank=True, max_length=2, verbose_name='C,C++,C#')),
                ('edu', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'lim")),
                ('edu_date', models.DateField(blank=True, null=True, verbose_name='talim,Sanasi')),
                ('work', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Ish')),
                ('work_date', models.DateField(blank=True, null=True, verbose_name='Ish,sanasi')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('note_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='note name')),
                ('note_body', models.TextField(blank=True, null=True, verbose_name='note body')),
                ('bg_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='colors', to='accounts.colors')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='jobs', to='accounts.jobs')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_profile',
                'verbose_name_plural': 'User_profiles',
            },
        ),
    ]
