from django.db import models
from django.contrib import admin
from django.forms import ModelForm, PasswordInput
import uuid


class Login(models.Model):
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) #not using an encryption for this prototype


class LoginForm(ModelForm):

    class Meta:
        model = Login
        widgets = {
            'password': PasswordInput(),
        }
        fields = ['username', 'password']


class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'unique_id', 'password')


admin.site.register(Login, LoginAdmin)


class FormPost(models.Model):
    name = models.CharField(max_length=150)
    food = models.TextField()
    music = models.TextField()
    movie = models.TextField()
    book = models.TextField()
    poem = models.TextField()
    quote = models.TextField()


class PostingForm(ModelForm):

    class Meta:
        model = FormPost
        fields = ['name', 'food', 'music', 'movie', 'book', 'poem', 'quote']


class FormPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'food', 'music', 'movie', 'book', 'poem', 'quote')


admin.site.register(FormPost, FormPostAdmin)