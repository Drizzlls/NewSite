from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article

class ArticlesPage(View):
    """ Страница 'Статьи' """
    template_name = 'article/articles/articles.html'

    def get(self, request):
        return render(request, self.template_name)

class ArticlePage(View):
    """ Страница Определенной статьи """
    template_name = 'article/articles/article.html'

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        return render(request, self.template_name, {'article': article,
                                                    'title': article.title_page,
                                                    'description':article.description_page,
                                                    'namePage': article.name_page})

