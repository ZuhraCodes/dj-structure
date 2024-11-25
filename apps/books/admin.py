from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from modeltranslation.admin import TranslationAdmin
from .models import Author, Book, BookReview

class BookReviewInlineAdmin(admin.TabularInline):
    model = BookReview
    autocomplete_fields = ("user", )
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("full_name", )

class BookAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'get_author_name') 
    # list_select_related = ('author', )
    search_fields = ('author__full_name', )
    inlines = (BookReviewInlineAdmin, )
    autocomplete_fields = ("author", )
    
    def get_author_name(self, obj):
        return obj.author.full_name
    
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        return super().get_queryset(request).select_related("author")
   
admin.site.register(Book, BookAdmin)

@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ("comment", )
    list_filter = ("book",)
