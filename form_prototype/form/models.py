from django.db import models
from django.contrib import admin
from django.forms import ModelForm


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