from django.shortcuts import render
from django.views import View

class IndexPage(View):
    """ Главная страница """
    template_name = 'pages/index.html'

    def get(self, request):
        return render(request, self.template_name)


class AboutPage(View):
    """ Страница 'О нас' """
    template_name = 'pages/about.html'

    def get(self, request):
        return render(request, self.template_name)

class NewsPage(View):
    """ Страница 'Новости' """
    template_name = 'pages/news.html'

    def get(self, request):
        return render(request, self.template_name)