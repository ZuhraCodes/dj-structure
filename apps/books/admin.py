from typing import Any
from django.contrib import admin
from django.db.models import Field
from django.forms import Field
from django.http import HttpRequest
from modeltranslation.admin import TranslationAdmin
from .models import Author, Book

class BookAdmin(TranslationAdmin):
    list_display = ('title', 'description',)
    group_fieldsets = True
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
