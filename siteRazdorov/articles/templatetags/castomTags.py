from django import template
from articles.models import Article

register = template.Library()

@register.simple_tag()
def getAllArcticles():
    """ Получаем все статьи """
    return Article.objects.all()[:4]