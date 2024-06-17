from django.contrib import admin
from .models import Article
from ckeditor.widgets import CKEditorWidget


admin.site.register(Article)

