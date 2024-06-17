from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=350, null=False, verbose_name='Название статьи')
    content = RichTextField()
