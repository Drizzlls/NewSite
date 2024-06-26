from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=350, null=False, verbose_name='Название статьи')
    content = RichTextField(verbose_name='Контент статьи')
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='images', verbose_name='Картинка в статье')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


class Client(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='ФИО')
    phone = models.CharField(max_length=20, null=False, verbose_name='Номер телефона')
    ip = models.CharField(max_length=20, null=False, verbose_name='IP')
    utm_source = models.CharField(max_length=20, null=True, blank=True, verbose_name='utm_source')
    utm_medium = models.CharField(max_length=20, null=True, blank=True, verbose_name='utm_medium')
    utm_campaign = models.CharField(max_length=20, null=True, blank=True, verbose_name='utm_campaign')
    utm_content = models.CharField(max_length=20, null=True, blank=True, verbose_name='utm_content')
    utm_term = models.CharField(max_length=20, null=True, blank=True, verbose_name='utm_term')
    date = models.DateTimeField(auto_now=True, verbose_name='Дата и время заявки')
    transitionSource = models.URLField(verbose_name='Источник перехода')
    page = models.URLField(verbose_name='Страница заявки')

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.phone