from django.contrib import admin
from .models import Article,Client
from ckeditor.widgets import CKEditorWidget

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'date', 'page')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Client, ClientAdmin)

