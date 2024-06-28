from django.db import models

class NameIntegrations(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название интеграции', unique=True)

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.title
class IntegrationsHook(models.Model):
    hook = models.CharField(max_length=350, verbose_name='API или Хук', unique=True)
    title = models.ForeignKey(NameIntegrations, on_delete=models.CASCADE, verbose_name='Сервис')

    class Meta:
        verbose_name = 'Ключ'
        verbose_name_plural = 'Ключи'

    def __str__(self):
        return self.title.title


