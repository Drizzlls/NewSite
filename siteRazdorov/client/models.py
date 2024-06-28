from django.db import models

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
