from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=350, null=False, verbose_name='Название статьи')
    content = RichTextField(verbose_name='Контент статьи')
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='images', verbose_name='Картинка в статье')
    title_page = models.CharField(max_length=150, verbose_name='Title страницы')
    description_page = models.CharField(max_length=150, verbose_name='Description страницы')
    name_page = models.CharField(max_length=150, verbose_name='Название страницы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


