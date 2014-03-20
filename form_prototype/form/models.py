from django.db import models
from django.contrib import admin
from django.forms import ModelForm, PasswordInput, Textarea, forms
import uuid

"""For the purposes of this prototype Login and Registration share the same Model """

class Login(models.Model):

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) #not using an encryption for this prototype


class LoginForm(ModelForm):

    class Meta:
        model = Login
        widgets = {
            'password': PasswordInput(),
        }
        fields = ['username', 'password']

class RegisterForm(ModelForm):

    class Meta:
        model = Login
        widgets = {
            'password': PasswordInput(),
        }
        fields = ['username', 'password']


class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


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
        widgets = {
            'food': forms.Textarea(attrs={'style': "width: 500px", 'rows': 10, }),
            'music': forms.Textarea(attrs={'style': "width: 500px", 'rows': 10, }),
            'movie': forms.Textarea(attrs={'style': "width: 500px", 'rows': 10, }),
            'book': forms.Textarea(attrs={'style': "width: 500px", 'rows': 10, }),
            'poem': forms.Textarea(attrs={'style': "width: 500px", 'rows': 10, }),
            'quote': forms.Textarea(attrs={'style': "width: 500px", 'rows': 10, }),
        }
        fields = ['name', 'food', 'music', 'movie', 'book', 'poem', 'quote']


class FormPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'food', 'music', 'movie', 'book', 'poem', 'quote')


admin.site.register(FormPost, FormPostAdmin)