from django.contrib import admin
from .models import Article
from ckeditor.widgets import CKEditorWidget

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Article, ArticleAdmin)


